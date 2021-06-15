import os
from paths import RANDO_ROOT_PATH
import yaml
from shutil import copyfile

from yaml.loader import FullLoader

class patch:
    def add_patches(self, options):
        rdir = options['output_folder']

        with open(RANDO_ROOT_PATH / 'patches.yaml') as patch_data:
            self.patch_data = yaml.load(patch_data, Loader=FullLoader)
        
        self.patches = self.patch_data['patches']

        for patch in self.patches:
            if float(options['version']) in patch['versions']:
                if patch['patch'] == 'entity':
                    patchfile = RANDO_ROOT_PATH / 'patches' / 'entities' / patch['patch_file']
                    patchdest = f'{rdir}/MobDropRandomizer/entities/' + patch['patch_file']
                    copyfile(patchfile, patchdest)