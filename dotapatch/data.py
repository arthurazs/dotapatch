from __future__ import print_function
import requests
from json import loads
from ast import literal_eval
from os import makedirs
import os.path as path


class HeropediaData(object):

    # CONSTANTS
    DATA_DIR = path.abspath(path.join(path.dirname(__file__), 'data'))
    ITEM_DATA = 'itemdata'
    HERO_DATA = 'herodata'

    # Initialization Functions
    @staticmethod
    def _downloadFile(name):
        link = 'http://www.dota2.com/jsfeed/heropediadata?feeds=' + name
        code = requests.get(link)
        dictionary = json.loads(code.text)[name]
        return dictionary

    @classmethod
    def _openFile(cls, name):
        with open(path.join(cls.DATA_DIR, name), 'r') as text:
            data = text.read()
            dictionary = literal_eval(data)
            return dictionary

    @classmethod
    def _saveFile(cls, name, content):
        with open(path.join(cls.DATA_DIR, name), 'w') as text:
            print(content, file=text)

    # Initialization
    def __init__(self):

        # Check data folder
        if not path.exists(self.DATA_DIR):
            makedirs(self.DATA_DIR)

        # Data Initialization
        if not path.isfile(path.join(self.DATA_DIR, self.ITEM_DATA)):
            self._item_dictionary = self._downloadFile(self.ITEM_DATA)
            self._saveFile(self.ITEM_DATA, self._item_dictionary)
        else:
            self._item_dictionary = self._openFile(self.ITEM_DATA)

        if not path.isfile(path.join(self.DATA_DIR, self.HERO_DATA)):
            self._hero_dictionary = self._downloadFile(self.HERO_DATA)
            self._saveFile(self.HERO_DATA, self._hero_dictionary)
        else:
            self._hero_dictionary = self._openFile(self.HERO_DATA)

    @staticmethod
    def sort_hero(hero_tuple):
        '''Return proper hero name.

        Formats hero_id to proper hero name.
        e.g. 'shredder' becomes 'timbersaw'

        Parameters
        ----------
        hero_tuple : tuple
            (name, _).

        Returns
        -------
        str
            Proper hero name.

        '''
        name = hero_tuple[0]    # gets hero name
        proper_name = {
            'wisp': 'io', 'abyssal_underlord': 'underlord',
            'obsidian_destroyer': 'outworld devourer',
            'shredder': 'timbersaw', 'nevermore': 'shadow fiend',
            'windrunner': 'windranger', 'zuus': 'zeus',
            'necrolyte': 'necrophos', 'skeleton_king': 'wraith king',
            'rattletrap': 'clockwerk', 'furion': 'natures prophet',
            'doom_bringer': 'doom', 'treant': 'treant protector',
            'magnataur': 'magnus'
        }

        return proper_name.get(name.lower(), name)

    @staticmethod
    def sort_item(item_tuple):
        '''Return proper item name.

        Formats item_id to proper item name.
        e.g. 'sphere' becomes 'linkens sphere'

        Parameters
        ----------
        item_tuple : tuple
            (name, _).

        Returns
        -------
        str
            Proper item name.

        '''
        name = item_tuple[0]    # gets item name
        proper_name = {
            'sphere': "linken s sphere",
        }

        return proper_name.get(name.lower(), name)

    # Default Function
    @staticmethod
    def _get_name(line, dictionary, proper_name):
        name = line.split(':')[0]
        name = name.lower().replace(' ', '_')
        found = dictionary.get(name, None)
        if not found:
            name = proper_name.get(name, None)
        return name

    # Name Functions
    def get_item_name(self, line):
        '''Return the item id.

        Search the line for an item name in item_dictionary and return
        its id.

        Parameters
        ----------
        line : str
            The phrase to be checked.

        Returns
        -------
        str
            Item id name.

        '''
        proper_name = {
            "linken's_sphere": 'sphere', 'battle_fury': 'bfury',
            'manta_style': 'manta',
            # 'aeon_disk': 'combo_breaker'
        }
        name = self._get_name(
            line,
            self._item_dictionary,
            proper_name)
        return name

    def get_hero_name(self, line):
        '''Return the hero name id.

        Search the line for an hero name in hero_dictionary and return
        its id.

        Parameters
        ----------
        line : str
            The phrase to be checked.

        Returns
        -------
        str
            Hero id name.

        '''
        proper_name = {
            'nightstalker': 'night_stalker', 'anti-mage': 'antimage',
            'underlord': 'abyssal_underlord', 'clockwerk': 'rattletrap',
            'windranger': 'windrunner', 'shadow_fiend': 'nevermore',
            'vengeful_spirit': 'vengefulspirit', 'drow': 'drow_ranger',
            "nature's_prophet": 'furion', 'necrophos': 'necrolyte',
            'wraith_king': 'skeleton_king'
        }
        name = self._get_name(
            line,
            self._hero_dictionary,
            proper_name)
        return name
