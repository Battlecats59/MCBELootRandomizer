import os
import json
import yaml

from typing import OrderedDict

from yaml.loader import FullLoader
from paths import RANDO_ROOT_PATH

class loot_tables:
    def get_loot_tables(self, options):
        with (RANDO_ROOT_PATH / 'loot_table_categories.yaml').open('r') as loot_tables:
            self.loot_table_list = yaml.load(loot_tables, Loader=FullLoader)

        self.randomized_mob_loot_table_list = []
        self.unrandomized_mob_loot_table_list = []
        self.randomized_chest_loot_table_list = []
        self.unrandomized_chest_loot_table_list = []

        for mob_lt in self.loot_table_list['entities']:
            if options['version'] in [str(ver) for ver in mob_lt['versions']]:
                if options['randomized_' + mob_lt['type']] == True:
                    self.randomized_mob_loot_table_list.append(mob_lt)
                else:
                    self.unrandomized_mob_loot_table_list.append(mob_lt)
            else:
                continue

        for chest_lt in self.loot_table_list['chests']:
            if options['version'] in [str(ver) for ver in chest_lt['versions']]:
                if options['randomized_' + chest_lt['type'] + '_chests'] == True:
                    self.randomized_chest_loot_table_list.append(chest_lt)
                else:
                    self.unrandomized_chest_loot_table_list.append(chest_lt)
            else:
                continue
                
        self.mob_loot_tables_list = self.randomized_mob_loot_table_list + self.unrandomized_mob_loot_table_list
        self.chest_loot_tables_list = self.randomized_chest_loot_table_list + self.unrandomized_chest_loot_table_list

        return self.randomized_mob_loot_table_list, self.unrandomized_mob_loot_table_list, self.randomized_chest_loot_table_list, self.unrandomized_chest_loot_table_list

    def read_loot_tables(self, mob_loot_table_list, chest_loot_table_list):
        self.loot_table_path = 'loot_tables'
        self.mob_r_loot_tables = []
        self.mob_s_loot_tables = []
        self.chest_r_loot_tables = []
        self.chest_s_loot_tables = []
        self.patched_mob_loot_table_list = []

        for m in mob_loot_table_list:
            with (RANDO_ROOT_PATH / self.loot_table_path / 'entities' / m['file']).open('r') as mlt:
                self.mob_loot_table = json.load(mlt)
                self.mob_r_loot_tables.append(self.mob_loot_table)
                if self.mob_loot_table == {}:
                    m['empty'] = True
                else:
                    m['empty'] = False
            self.mob_s_loot_tables.append(m['name'])
            self.patched_mob_loot_table_list.append(m)

        for c in chest_loot_table_list:
            with (RANDO_ROOT_PATH / self.loot_table_path / 'chests' / c['file']).open('r') as clt:
                self.chest_r_loot_tables.append(json.load(clt))
            self.chest_s_loot_tables.append(c['name'])

        return self.mob_r_loot_tables, self.mob_s_loot_tables, self.chest_r_loot_tables, self.chest_s_loot_tables, self.patched_mob_loot_table_list

    def write_loot_tables(self, mob_loot_tables, mob_s_loot_tables, chest_loot_tables, chest_s_loot_tables):

        self.mob_loot_tables_names = []
        self.mob_loot_tables_files = []
        self.chest_loot_tables_names = []
        self.chest_loot_tables_files = []

        for mlt in self.mob_loot_tables_list:
            self.mob_loot_tables_names.append(mlt['name'])
            self.mob_loot_tables_files.append(mlt['file'])

        for clt in self.chest_loot_tables_list:
            self.chest_loot_tables_names.append(clt['name'])
            self.chest_loot_tables_files.append(clt['file'])

        self.patched_mob_loot_tables = OrderedDict(zip(self.mob_loot_tables_files, mob_loot_tables))
        self.spoiler_mob_loot_tables = OrderedDict(zip(self.mob_loot_tables_names, mob_s_loot_tables))
        self.patched_chest_loot_tables = OrderedDict(zip(self.chest_loot_tables_files, chest_loot_tables))
        self.spoiler_chest_loot_tables = OrderedDict(zip(self.chest_loot_tables_names, chest_s_loot_tables))

        return self.patched_mob_loot_tables, self.spoiler_mob_loot_tables, self.patched_chest_loot_tables, self.spoiler_chest_loot_tables