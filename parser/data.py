from __future__ import print_function
import requests
import ast
import os
import os.path as path


class HeropediaData (object):

    # CONSTANTS
    DATA_DIR = path.abspath(path.join(path.dirname(__file__), 'data'))
    ITEM_DATA = 'itemdata'
    HERO_DATA = 'herodata'
    ABILITY_DATA = 'abilitydata'

    # Initialization Functions
    @staticmethod
    def _downloadFile(name):
        link = 'http://www.dota2.com/jsfeed/heropediadata?feeds=' + name
        code = requests.get(link)
        data = code.text.replace('{"' + name + '":', '') \
            .replace('}}', '}').replace(':false', ':False') \
            .replace(':null', ':None').replace(':true', ':True')
        dictionary = ast.literal_eval(data)
        return dictionary

    @staticmethod
    def _openFile(name):
        with open(path.join(HeropediaData.DATA_DIR, name), 'r') as text:
            data = text.read()
            dictionary = ast.literal_eval(data)
            return dictionary

    @staticmethod
    def _saveFile(name, content):
        with open(path.join(HeropediaData.DATA_DIR, name), 'w') as text:
            print(content, file=text)

    # Initialization
    def __init__(self):
        # Check data folder
        if not path.exists(HeropediaData.DATA_DIR):
            os.makedirs(HeropediaData.DATA_DIR)

        # Data Initialization
        if not path.isfile(path.join(
                HeropediaData.DATA_DIR, HeropediaData.ITEM_DATA)):
            self._item_dictionary = HeropediaData._downloadFile(
                HeropediaData.ITEM_DATA)
            HeropediaData._saveFile(
                HeropediaData.ITEM_DATA, self._item_dictionary)
        else:
            self._item_dictionary = HeropediaData._openFile(
                HeropediaData.ITEM_DATA)

        if not path.isfile(path.join(
                HeropediaData.DATA_DIR, HeropediaData.HERO_DATA)):
            self._hero_dictionary = HeropediaData._downloadFile(
                HeropediaData.HERO_DATA)
            HeropediaData._saveFile(
                HeropediaData.HERO_DATA, self._hero_dictionary)
        else:
            self._hero_dictionary = HeropediaData._openFile(
                HeropediaData.HERO_DATA)

        if not path.isfile(path.join(
                HeropediaData.DATA_DIR, HeropediaData.ABILITY_DATA)):
            self._ability_dictionary = HeropediaData._downloadFile(
                HeropediaData.ABILITY_DATA)
            HeropediaData._saveFile(
                HeropediaData.ABILITY_DATA, self._ability_dictionary)
        else:
            self._ability_dictionary = HeropediaData._openFile(
                HeropediaData.ABILITY_DATA)

    @staticmethod
    def sort(hero_tuple):
        '''Return proper hero name.

        Formats hero_name_id to proper hero name.
        e.g. 'shredder' becomes 'timbersaw'

        Parameters
        ----------
        hero_tuple : tuple
            (name, value).

        Returns
        -------
        str
            Proper hero name.

        '''
        name = hero_tuple[0]    # gets hero name
        proper_name = {
            'wisp': 'io', 'abyssal_underlord': 'underlord',
            'obsidian_destroyer': 'outworld_devourer',
            'shredder': 'timbersaw', 'nevermore': 'shadow_fiend',
            'windrunner': 'windranger', 'zuus': 'zeus',
            'necrolyte': 'necrophos', 'skeleton_king': 'wraith_king',
            'rattletrap': 'clockwerk', 'furion': 'natures_prophet',
            'doom_bringer': 'doom', 'treant': 'treant_protector',
            'centaur': 'centaur_warrunner', 'magnataur': 'magnus'
        }

        return proper_name.get(name.lower(), name)

    # Handle name bugs
    @staticmethod
    def _prepare_d_name(line):
        '''Format [line] and return proper dname.

        Formats [line] to proper dname.
        e.g. 'starfall something' becomes 'starstorm'
        e.g. "nyx's something" becomes "nyx assassin"
        e.g. 'RiKi' becomes 'riki'
        e.g. 'riki' remains 'riki'

        Parameters
        ----------
        line : list
            Changelog line split by spaces.

        Returns
        -------
        str.lower()
            Formatted dname all lowercase.

        '''
        name = line[0].lower().replace('\'s', '')
        proper_name = {
            'drow': 'drow ranger', 'nyx': 'nyx assassin',
            'centaur': 'centaur warrunner', 'starfall': 'starstorm',
            'smokescreen': 'smoke screen'
        }
        return proper_name.get(name, ' '.join(line).lower())

    @staticmethod
    def _prepare_h_url(h_url):
        '''Format h_url if necessary.

        e.g. 'io' becomes 'wisp'
        e.g. 'RiKi' becomes 'riki'
        e.g. 'riki' remains 'riki'

        Parameters
        ----------
        h_url : string
            value['hurl'].

        Returns
        -------
        str.lower()
            Formatted h_url all lowercase.

        '''
        proper_name = {
            'io': 'wisp', 'underlord': 'abyssal_underlord',
            'centaur_warrunner': 'centaur', 'anti-mage': 'antimage',
            'queen_of_pain': 'queenofpain'
        }
        return proper_name.get(h_url.lower(), h_url.lower())

    @staticmethod
    def _prepare_item(key):
        '''Format key if necessary.

        e.g. 'dIfFuSaL_bLaDe_2' becomes 'diffusal_blade'
        e.g. 'DrAgOn_LaNcE' becomes 'dragon_lance'

        Parameters
        ----------
        key : string
            item_dictionary.key.

        Returns
        -------
        str.lower()
            Formatted key all lowercase.

        '''
        proper_name = {
            'diffusal_blade_2': 'diffusal_blade'
        }
        return proper_name.get(key.lower(), key.lower())

    @staticmethod
    def _prepare_ability(line):
        '''
        Checks [line] for common abilities and returns the proper hero.

        Checks the changelog line for common abilities. If it finds a
        common ability, checks the line for a hero name and return the
        hero's dname.
        e.g. Both Anti-Mage and Queen of Pain have a 'blink' ability.

        Parameters
        ----------
        line : list
            Line from the changelog.

        Returns
        -------
        str
            Hero d_name.

        '''
        text = ' '.join(line).lower()
        name = None
        if 'return' in text:
            if 'centaur' in text:
                name = 'centaur_warrunner'
            elif 'kunkka' in text:
                name = 'kunkka'
        elif 'blink strike' in text:
            name = 'riki'
        elif 'blink' in text:
            if 'anti-mage' in text:
                name = 'anti-mage'
            elif 'queen of pain' in text:
                name = 'queen_of_pain'
        return name

    # Default Function
    def _get_name(self, line, dictionary):
        name = HeropediaData._prepare_line(line)
        for key, value in dictionary.items():
            length = len(value['dname'].split(' '))
            ability_hero = HeropediaData._prepare_ability(name)
            if (ability_hero and 'hurl' in value):
                if (value['hurl'].lower() == ability_hero and
                        HeropediaData._prepare_d_name(name[:length]) ==
                        value['dname'].lower()):
                    return (HeropediaData._prepare_item(key), value)
            else:
                if (HeropediaData._prepare_d_name(name[:length]) ==
                        value['dname'].lower()):
                    return (HeropediaData._prepare_item(key), value)
        return (None, None)

    @staticmethod
    def _prepare_line(line):
        '''Returns line as list whilst removing unnecessary words.

        e.g. "Fixed Centaur's bug" becomes "Centaur's bug"

        Parameters
        ----------
        line : str
            Changelog line.

        Returns
        -------
        list
            List formatted if necessary.

        '''
        # TODO remove from get_*_name()/get_ability_*()
        #      and put under _get_name()
        names = line.split()
        name = None
        if names[0].lower() == 'fixed':
            name = names[1:]
        else:
            name = names[:]
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
        key, _ = self._get_name(line, self._item_dictionary)
        return key

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
        key, _ = self._get_name(line, self._hero_dictionary)
        return key

    def get_ability_hero(self, line):
        '''Return the hero name id given its ability.

        Search the line for an ability name in hero_dictionary and
        return its hero's id.

        Parameters
        ----------
        line : str
            The phrase to be checked.

        Returns
        -------
        str
            Hero id name.

        '''
        _, value = self._get_name(line, self._ability_dictionary)
        if value:
            return HeropediaData._prepare_h_url(value['hurl'])
        else:
            return None
