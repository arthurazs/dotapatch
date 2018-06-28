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

    HERO_NAME = {
        'night_stalker': 'nightstalker', 'antimage': 'anti-mage',
        'abyssal_underlord': 'underlord', 'rattletrap': 'clockwerk',
        'windrunner': 'windranger', 'nevermore': 'shadow_fiend',
        'vengefulspirit': 'vengeful_spirit', 'drow_ranger': 'drow',
        'furion': "nature's_prophet", 'necrolyte': 'necrophos',
        'skeleton_king': 'wraith_king', 'zuus': 'zeus', 'doom_bringer': 'doom',
        'magnataur': 'magnus', 'wisp': 'io', 'centaur': 'centaur_warrunner',
        'treant': 'treant_protector', 'shredder': 'timbersaw',
        'obsidian_destroyer': 'outworld_devourer',
        'life_stealer': 'lifestealer', 'queenofpain': 'queen_of_pain',
    }
    ITEM_NAME = {
        'sphere': "linken's_sphere", 'bfury': 'battle_fury',
        'manta': 'manta_style', 'courier': 'animal_courier',
        'boots': 'boots_of_speed', 'basher': 'skull_basher',
        'refresher': 'refresher_orb', 'heart': 'heart_of_tarrasque',
        'blink': 'blink_dagger', 'travel_boots': 'boots_of_travel',
        'ward_observer': 'observer_ward', 'vladmir': "vladmir's_offering",
        'heavens_halberd': "heaven's_halberd", 'ward_sentry': 'sentry_ward',
        'cyclone': "eul's_scepter_of_divinity", 'tpscroll': 'tp_scroll'
        # 'combo_breaker': 'aeon_disk'
    }

    _logger = get_logger('dotapatch.data')

    # Initialization Functions
    @classmethod
    def _download_file(cls, name):
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

    @staticmethod
    def _key_to_value(dic):
        '''Maps key to value from a dictionary.

        e.g. {1: 'asd'} to {'asd': 1}

        Parameters
        ----------
        dic : dict
            Dictionary to be mapped

        Returns
        -------
        dict
            Mapped dictionary

        '''
        return {value: key for key, value in dic.items()}

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

        # Proper Name Initialization
        self._proper_hero_name = self._key_to_value(self.HERO_NAME)
        self._proper_item_name = self._key_to_value(self.ITEM_NAME)

    @classmethod
    def sort_hero(cls, hero_tuple):
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
        return cls.HERO_NAME.get(name.lower(), name)

    @classmethod
    def sort_item(cls, item_tuple):
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
        return cls.ITEM_NAME.get(name.lower(), name)

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
        name = self._get_name(
            line,
            self._item_dictionary,
            self._proper_item_name)
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
        name = self._get_name(
            line,
            self._hero_dictionary,
            self._proper_hero_name)
        return name
