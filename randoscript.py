import os
import random
import yaml
from yaml import FullLoader
import hashlib

from packedbits import PackedBitsWriter, PackedBitsReader
from logic.logic import logic
from loot_tables import loot_tables
from pack_build import build
from paths import RANDO_ROOT_PATH

class randomize:
    def __randomize__(self, options):
        self.rng = random.Random()
        self.rng.seed(options['seed'])

        options['hash'] = randomize.rando_hash(self, options)
        options['permalink'] = randomize.get_permalink(self, options)

        self.mob_loot_table_list, self.unrandomized_mob_loot_table_list, self.chest_loot_table_list, self.unrandomized_chest_loot_table_list = loot_tables.get_loot_tables(self, options)

        self.rng.shuffle(self.mob_loot_table_list)
        self.rng.shuffle(self.chest_loot_table_list)
        self.mob_loot_table_list.extend(self.unrandomized_mob_loot_table_list)
        self.chest_loot_table_list.extend(self.unrandomized_chest_loot_table_list)

        self.mob_loot_tables, self.s_mob_loot_tables, self.chest_loot_tables, self.s_chest_loot_tables, self.mob_loot_table_list = loot_tables.read_loot_tables(self, self.mob_loot_table_list, self.chest_loot_table_list)

        #self.v_loot_tables = logic.logic_expression(self, self.v_loot_tables)
            # Logic is a WIP

        self.mob_patched_loot_tables, self.spoiler_mob_loot_tables, self.chest_patched_loot_tables, self.spoiler_chest_loot_tables = loot_tables.write_loot_tables(self, self.mob_loot_tables, self.s_mob_loot_tables, self.chest_loot_tables, self.s_chest_loot_tables)

        pack_build = build.build_pack(self, options, self.mob_patched_loot_tables, self.chest_patched_loot_tables)

        build.write_spoiler_log(self, options, self.spoiler_mob_loot_tables, self.spoiler_chest_loot_tables, self.mob_loot_table_list)
            #functional, but off until a UI option is created

        return (pack_build, options)

    def rando_hash(self, options):  # From https://github.com/lepelog/sslib
        rando_hash = hashlib.md5()
        rando_hash.update(str(options['seed']).encode('ASCII'))
        rando_hash.update(randomize.get_permalink(self, options).encode('ASCII'))
        with open(RANDO_ROOT_PATH / 'version.txt') as VERSION:
            rando_hash.update(VERSION.read().strip().encode('ASCII'))
        with open(RANDO_ROOT_PATH / 'hashnames.txt') as f:
            names = [s.strip() for s in f.readlines()]
        hash_random = random.Random()
        hash_random.seed(rando_hash.digest())
        return ' '.join(hash_random.choice(names) for _ in range(3))

    def get_permalink(self, options):  # From https://github.com/lepelog/sslib
        with (RANDO_ROOT_PATH / 'gui/options.yaml').open('r') as optf:
            OPTIONS = yaml.load(optf, Loader=FullLoader)

        writer = PackedBitsWriter()
        for option in OPTIONS:
            if not option.get('permalink', True):
                continue
            value = options[option['option']]
            if option['type'] == 'boolean':
                # one bit
                writer.write(int(value), 1)
            elif option['type'] == 'int':
                # needs information, how many bits this number is
                writer.write(value, option['bits'])
            elif option['type'] == 'multichoice':
                # as many bits as choices
                for choice in option['choices']:
                    writer.write(int(choice in value), 1)
            elif option['type'] == 'singlechoice':
                # needs information, how many bits this number is, then it's just the index to the choices
                if option['option'] == 'version':
                    writer.write([str(c) for c in option['choices']].index(value), option['bits'])
                else:
                    writer.write(option['choices'].index(value), option['bits'])
            else:
                raise Exception(f'unknown type: {option["type"]}')
        writer.flush()
        permalink = writer.to_base64()
        #if self['seed'] != -1:
        #    permalink += "#" + str(self['seed'])
        return permalink