import os
import yaml
import json
from yaml.loader import FullLoader

class logic:
    def logic_expression(self, loot_tables):
        self.logic = yaml.load('./logic.yaml', Loader=FullLoader)
        self.logic = self.logic['logic']

        for logic_expression in self.logic:
            self.logic_name = logic_expression['name']
            self.logic_file = logic_expression['file']
            self.logic_requirements = logic_expression['requires']

            for requirement in self.logic_requirements:
                with open(f'../loot_tables/{requirement}.json') as self.logic_template:
                    self.logic_default = json.load(self.logic_template)
                    # WORK IN PROGRESS