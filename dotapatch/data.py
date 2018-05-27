'''Module for the heropediadata api.'''
from __future__ import print_function
from json import loads
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
from contextlib import closing
from ast import literal_eval
from os import makedirs
import os.path as path
from logging import getLogger as get_logger


class HeropediaData(object):
    '''Uses dota2's heropediadata api to find the correct hero/item name.'''

    # CONSTANTS
    DATA_DIR = path.abspath(path.join(path.dirname(__file__), 'data'))
    ITEM_DATA = 'itemdata'
    HERO_DATA = 'herodata'

    _logger = get_logger('dotapatch.data')

    # Initialization Functions
    @classmethod
    def download_file(cls, name):
        '''Parses dota2's heropediadata file into dict.

        Parameters
        ----------
        name : str
            heropediadata feed to be downloaded

        Returns
        -------
        dictionary : dict
            heropediadata
        '''
        cls._logger.info(
            "Downloading {} from dota2's heropediadata".format(name))
        link = 'http://www.dota2.com/jsfeed/heropediadata?feeds=' + name
        try:
            if 'file:///' in link:
                raise ValueError('urlopen trying to leak information')
        except ValueError as err:
            cls._logger.critical('{}: {}'.format(err.__class__.__name__, err))
            raise SystemExit(-1)
        with closing(urlopen(link)) as response:
            content = response.read()
        json_data = content.decode('utf-8')
        dictionary = loads(json_data)
        cls._save_file(name, dictionary[name])
        cls._logger.info("Updated {} saved successfully".format(name))
        return dictionary[name]

    @classmethod
    def _open_file(cls, name):
        '''Open dotapatch's heropediadata file.

        Parameters
        ----------
        name : str
            heropediadata file to be opened

        Returns
        -------
        dictionary : dict
            heropediadata
        '''
        with open(path.join(cls.DATA_DIR, name), 'r') as text:
            data = text.read()
            dictionary = literal_eval(data)
            return dictionary

    @classmethod
    def _save_file(cls, name, content):
        '''Stores heropediadata file.

        Parameters
        ----------
        name : str
            heropediadata file name to be created

        content : str
            heropediadata content to be stored
        '''
        with open(path.join(cls.DATA_DIR, name), 'w') as text:
            print(content, file=text)

    # Initialization
    def __init__(self):
        '''Initializes HeropediaData.

        Check if heropediadata files exist.
        If a file is not found, it's downloaded from dota2 heropediadata feed.
        '''

        # Check data folder
        if not path.exists(self.DATA_DIR):
            makedirs(self.DATA_DIR)

        # Data Initialization
        if not path.isfile(path.join(self.DATA_DIR, self.ITEM_DATA)):
            self._item_dictionary = self.download_file(self.ITEM_DATA)
        else:
            self._item_dictionary = self._open_file(self.ITEM_DATA)

        if not path.isfile(path.join(self.DATA_DIR, self.HERO_DATA)):
            self._hero_dictionary = self.download_file(self.HERO_DATA)
        else:
            self._hero_dictionary = self._open_file(self.HERO_DATA)

    @staticmethod
    def sort_hero(hero_tuple):
        '''Formats hero_id to proper hero name.

        Note
        ----
        ``shredder`` returns ``timbersaw``

        Parameters
        ----------
        hero_tuple : tuple
            (name, _)

        Returns
        -------
        name : str
            Proper hero name

        '''
        name, _ = hero_tuple
        proper_name = {
            'wisp': 'io', 'abyssal_underlord': 'underlord',
            'obsidian_destroyer': 'outworld devourer',
            'shredder': 'timbersaw', 'nevermore': 'shadow fiend',
            'windrunner': 'windranger', 'zuus': 'zeus',
            'necrolyte': 'necrophos', 'skeleton_king': 'wraith king',
            'rattletrap': 'clockwerk', 'furion': 'natures prophet',
            'doom_bringer': 'doom', 'treant': 'treant protector',
            'magnataur': 'magnus', 'shredder': 'timbersaw',
        }

        return proper_name.get(name.lower(), name)

    @staticmethod
    def sort_item(item_tuple):
        '''Formats item_id to proper item name.

        Note
        ----
        ``sphere`` returns ``linkens sphere``

        Parameters
        ----------
        item_tuple : tuple
            (name, _)

        Returns
        -------
        name : str
            Proper item name

        '''
        name, _ = item_tuple
        proper_name = {
            'sphere': "linken s sphere",
            'courier': 'animal courier',
            'basher': 'skull_basher',
            'blink': 'blink_dagger', 'travel_boots': 'boots_of_travel',
            'ward_sentry': 'sentry_ward', 'ward_observer': 'observer_ward',
        }

        return proper_name.get(name.lower(), name)

    # Default Function
    @staticmethod
    def _get_name(line, dictionary, proper_name):
        '''Default function for finding object name.

        Splits the line by ':' and checks if it exists in the object's
        dictionary (heropediadata).

        Note
        ----
        ``Illusions attack damage reduced against buildings`` returns ``None``

        Parameters
        ----------
        line : str
            The phrase to be checked

        dictionary : dict
            Object's main dictionary (heropediadata)

        proper_name : dict
            Object's secondary dictionary

        Returns
        -------
        name : str or None
            Proper object name
        '''
        name = line.split(':')[0]
        name = name.lower().replace(' ', '_')
        found = dictionary.get(name, None)
        if not found:
            name = proper_name.get(name, None)
        return name

    # Name Functions
    def get_item_name(self, line):
        '''Searches the line for an item name and returns its proper name.

        Note
        ----
        ``Dragon Lance: strength reduced from 14 to 13`` returns
        ``dragon_lance``

        Parameters
        ----------
        line : str
            The phrase to be checked

        Returns
        -------
        name : str or None
            Proper item name
        '''
        proper_name = {
            "linken's_sphere": 'sphere', 'battle_fury': 'bfury',
            'manta_style': 'manta', 'animal_courier': 'courier',
            'boots_of_speed': 'boots', 'skull_basher': 'basher',
            'refresher_orb': 'refresher', 'heart_of_tarrasque': 'heart',
            'blink_dagger': 'blink', 'boots_of_travel': 'travel_boots',
            'observer_ward': 'ward_observer', "vladmir's_offering": 'vladmir',
            "heaven's_halberd": 'heavens_halberd',
            'sentry_ward': 'ward_sentry',
            # 'aeon_disk': 'combo_breaker'
        }

        name = self._get_name(
            line,
            self._item_dictionary,
            proper_name)
        return name

    def get_hero_name(self, line):
        '''Searches the line for a hero name and returns its proper name.

        Note
        ----
        ``Juggernaut: base damage reduced by 2`` returns ``juggernaut``

        Parameters
        ----------
        line : str
            The phrase to be checked

        Returns
        -------
        name : str or None
            Proper hero name
        '''
        proper_name = {
            'nightstalker': 'night_stalker', 'anti-mage': 'antimage',
            'underlord': 'abyssal_underlord', 'clockwerk': 'rattletrap',
            'windranger': 'windrunner', 'shadow_fiend': 'nevermore',
            'vengeful_spirit': 'vengefulspirit', 'drow': 'drow_ranger',
            "nature's_prophet": 'furion', 'necrophos': 'necrolyte',
            'wraith_king': 'skeleton_king', 'zeus': 'zuus',
            'doom': 'doom_bringer', 'magnus': 'magnataur', 'io': 'wisp',
            'centaur_warrunner': 'centaur', 'treant_protector': 'treant',
            'outworld_devourer': 'obsidian_destroyer', 'timbersaw': 'shredder',
            'lifestealer': 'life_stealer', 'queen_of_pain': 'queenofpain'
        }
        name = self._get_name(
            line,
            self._hero_dictionary,
            proper_name)
        return name
