import os
from paths import RANDO_ROOT_PATH
import uuid
import json
import yaml
import shutil
from pack_patches import patch

from yaml.loader import FullLoader

class build:
    def build_pack(self, options, patched_mob_loot_tables, patched_chest_loot_tables):

        # Variables
        rdir = options['output_folder']
        rseed = options['seed']
        rpreset = options['preset']
        rmcversion = options['version']
        rhash = options['hash']
        rpermalink = options['permalink']

            # Setup directories
        if os.path.isdir(f'{rdir}/MobDropRandomizer/') == True:
            shutil.rmtree(f'{rdir}/MobDropRandomizer/')
        os.mkdir(f'{rdir}/MobDropRandomizer/')
        os.mkdir(f'{rdir}/MobDropRandomizer/loot_tables/')
        os.mkdir(f'{rdir}/MobDropRandomizer/loot_tables/entities/')
        os.mkdir(f'{rdir}/MobDropRandomizer/loot_tables/chests/')
        os.mkdir(f'{rdir}/MobDropRandomizer/loot_tables/chests/village/')
        os.mkdir(f'{rdir}/MobDropRandomizer/entities/')


        # Version
        with open(RANDO_ROOT_PATH / 'version.txt') as versionfile:
            version = versionfile.read().strip()


        # Edit manifest.json
        with open(RANDO_ROOT_PATH / 'behavior_pack_files/manifest.json') as manifest:
            manifestData = json.load(manifest)
        
        headerData = manifestData.get('header')
        moduleData = manifestData.get('modules')

            # uuids
        headerData.update({'uuid': str(uuid.uuid4())})
        moduleData[0].update({'uuid': str(uuid.uuid4())})

            # title/desc
        headerData.update({"name": f"MCBE Loot Randomizer v{version}"})
        headerData.update({"description": f"{rmcversion} | Rando Seed: {rseed}, Rando Hash: {rhash}, Rando Settings: {rpreset} [{rpermalink}]"})

        manifestData.update({'header': headerData, 'modules': moduleData})


        # Patches
        patch.add_patches(self, options)

        
        # Writing to file
        manifestFile = open(f'{rdir}/MobDropRandomizer/manifest.json', 'w')
        manifestFile.write(json.dumps(manifestData, indent=2).replace("'", '"'))
        manifestFile.close()
        shutil.copyfile(RANDO_ROOT_PATH / 'behavior_pack_files/pack_icon.png', f'{rdir}/MobDropRandomizer/pack_icon.png')

        for mlt, mplt in patched_mob_loot_tables.items():
            mltFile = open(f'{rdir}/MobDropRandomizer/loot_tables/entities/{mlt}', 'w')
            mltFile.write(json.dumps(mplt, indent=2).replace("'", '"'))
            mltFile.close()
        
        for clt, cplt in patched_chest_loot_tables.items():
            if clt.startswith('village_'):
                cltFile = open(f'{rdir}/MobDropRandomizer/loot_tables/chests/village/{clt}', 'w')
                cltFile.write(json.dumps(cplt, indent=2).replace("'", '"'))
                cltFile.close()
            else:
                cltFile = open(f'{rdir}/MobDropRandomizer/loot_tables/chests/{clt}', 'w')
                cltFile.write(json.dumps(cplt, indent=2).replace("'", '"'))
                cltFile.close()
        
        return (True)

    def write_spoiler_log(self, options, spoiler_mob_loot_tables, spoiler_chest_loot_tables, mob_loot_table_data):

        rdir = options['output_folder']
        rseed = options['seed']
        rpreset = options['preset']
        rhash = options['hash']
        rpermalink = options['permalink']

        if options['spoiler_log'] == False:
            if os.path.exists(f'{rdir}/MobDropRandomizer/spoiler_log.txt'):
                os.remove(f'{rdir}/MobDropRandomizer/spoiler_log.txt')
                return
            else:
                return

        with open(RANDO_ROOT_PATH / 'version.txt') as versionfile:
            version = versionfile.read().strip()

        self.spoiler_log = f'MCBE Loot Randomizer v{version}\nRandomizer Seed: {rseed}\nRandomizer Hash: {rhash}\n\nRandomizer Option Preset: {rpreset}\nSettings Permalink: {rpermalink}\n\nSettings:\n'

        for optkey, opt in options.items():
            if optkey == 'hash' or optkey == 'permalink':
                continue
            else:
                self.spoiler_log += f'  {optkey}: {opt}\n'

        self.spoiler_log += '\nThe mob on the left will drop the loot of the mob on the right.\nSome mobs can have an empty loot table.\n\n'

        for check, loot in spoiler_mob_loot_tables.items():
            self.append_to_spoiler_log = f'{check}:                                     {loot}'
            for mlt in mob_loot_table_data:
                if mlt['name'] == loot:
                    if mlt['empty'] == True:
                        self.append_to_spoiler_log += ' (Empty)\n'      
                    else:
                        self.append_to_spoiler_log += '\n' 
            self.spoiler_log += self.append_to_spoiler_log

        self.spoiler_log += '\nThe chest on the left will contain the loot of the chest on the right.\n\n'

        for check, loot in spoiler_chest_loot_tables.items():
            self.append_to_spoiler_log = f'{check}:                                     {loot}\n'
            self.spoiler_log += self.append_to_spoiler_log

        spoilerlogfile = open(f'{rdir}/MobDropRandomizer/spoiler_log.txt', 'w')
        spoilerlogfile.write(self.spoiler_log)
        spoilerlogfile.close()