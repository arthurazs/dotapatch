from __future__ import print_function
import requests
import ast
import os
import os.path as path


class HeropediaData (object):

    # CONSTANTS
    _DATA_DIR = path.abspath(path.join(path.dirname(__file__), 'data'))
    ITEM_DATA = 'itemdata'
    HERO_DATA = 'herodata'
    ABILITY_DATA = 'abilitydata'

    # Initialization Functions
    def _downloadFile(self, name):
        link = 'http://www.dota2.com/jsfeed/heropediadata?feeds=' + name
        code = requests.get(link)
        data = code.text.replace('{"' + name + '":', '') \
            .replace('}}', '}').replace(':false', ':False') \
            .replace(':null', ':None').replace(':true', ':True')
        dictionary = ast.literal_eval(data)
        return dictionary

    def _openFile(self, name):
        with open(path.join(self._DATA_DIR, name), 'r') as text:
            data = text.read()
            dictionary = ast.literal_eval(data)
            return dictionary

    def _saveFile(self, name, content):
        with open(path.join(self._DATA_DIR, name), 'w') as text:
            print(content, file=text)

    # Initialization
    def __init__(self):
        # Check data folder
        if not path.exists(self._DATA_DIR):
            os.makedirs(self._DATA_DIR)

        # Data Initialization
        if not path.isfile(path.join(self._DATA_DIR, self.ITEM_DATA)):
            self._item_dictionary = self._downloadFile(self.ITEM_DATA)
            self._saveFile(self.ITEM_DATA, self._item_dictionary)
        else:
            self._item_dictionary = self._openFile(self.ITEM_DATA)

        if not path.isfile(path.join(self._DATA_DIR, self.HERO_DATA)):
            self._hero_dictionary = self._downloadFile(self.HERO_DATA)
            self._saveFile(self.HERO_DATA, self._hero_dictionary)
        else:
            self._hero_dictionary = self._openFile(self.HERO_DATA)

        if not path.isfile(
          path.join(self._DATA_DIR, self.ABILITY_DATA)):
            self._ability_dictionary = self._downloadFile(
                self.ABILITY_DATA)
            self._saveFile(self.ABILITY_DATA, self._ability_dictionary)
        else:
            self._ability_dictionary = self._openFile(self.ABILITY_DATA)

    @staticmethod
    def sort(dictionary):
        name = dictionary[0]
        if (name.lower() == 'wisp'):
            return 'io'
        elif (name.lower() == 'abyssal_underlord'):
            return 'underlord'
        elif (name.lower() == 'obsidian_destroyer'):
            return 'outworld_devourer'
        elif (name.lower() == 'shredder'):
            return 'timbersaw'
        elif (name.lower() == 'nevermore'):
            return 'shadow_fiend'
        elif (name.lower() == 'windrunner'):
            return 'windranger'
        elif (name.lower() == 'zuus'):
            return 'zeus'
        elif (name.lower() == 'necrolyte'):
            return 'necrophos'
        elif (name.lower() == 'skeleton_king'):
            return 'wraith_king'
        elif (name.lower() == 'rattletrap'):
            return 'clockwerk'
        elif (name.lower() == 'furion'):
            return 'natures_prophet'
        elif (name.lower() == 'doom_bringer'):
            return 'doom'
        elif (name.lower() == 'treant'):
            return 'treant_protector'
        elif (name.lower() == 'centaur'):
            return 'centaur_warrunner'
        elif (name.lower() == 'magnataur'):
            return 'magnus'
        return name

    # Handle name bugs
    def _checkDname(self, name):
        name[0] = name[0].lower().replace('\'s', '')
        if (name[0].lower() == 'drow'):
            return 'drow ranger'
        if (name[0].lower() == 'nyx'):
            return 'nyx assassin'
        if (name[0].lower() == 'centaur'):
            return 'centaur warrunner'
        elif (name[0].lower() == 'smokescreen'):
            return 'smoke screen'
        elif (name[0].lower() == 'starfall'):
            return 'starstorm'
        return ' '.join(name).lower()

    def _checkHurl(self, name):
        if (name.split()[0].lower() == 'io'):
            return 'wisp'
        if (name.split()[0].lower() == 'underlord'):
            return 'abyssal_underlord'
        if (name.split()[0].lower() == 'centaur_warrunner'):
            return 'centaur'
        if (name.split()[0].lower() == 'queen_of_pain'):
            return 'queenofpain'
        if (name.split()[0].lower() == 'anti-mage'):
            return 'antimage'
        return name

    def _checkItem(self, name):
        if (name.lower() == 'diffusal_blade_2'):
            return 'diffusal_blade'
        return name

    def _checkAbility(self, text):
        name = ' '.join(text).lower()
        if 'return' in name:
            if 'centaur' in name:
                return 'centaur_warrunner'
            elif 'kunkka' in name:
                return 'kunkka'
        elif 'blink strike' in name:
            return 'riki'
        elif 'blink' in name:
            if 'anti-mage' in name:
                return 'anti-mage'
            elif 'queen of pain' in name:
                return 'queen_of_pain'
        return None

    # Default Function
    def _get_name(self, name, dictionary):
        for key, value in dictionary.items():
            length = len(value['dname'].split(' '))
            ability_hero = self._checkAbility(name)
            if (ability_hero and 'hurl' in value):
                if (
                  value['hurl'].lower() == ability_hero and
                  self._checkDname(name[:length]) == value['dname']
                  .lower()):
                    return (self._checkItem(key), value)
            else:
                if (
                  self._checkDname(name[:length]) == value['dname']
                  .lower()):
                    return (self._checkItem(key), value)
        return (None, None)

    # Checks if the line starts with fixed and removes it
    @classmethod
    def _prepare_name(cls, value):
        names = value.split(' ')
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
        name = self._prepare_name(line)
        return self._get_name(name, self._item_dictionary)[0]

    def get_hero_name(self, line):
        name = self._prepare_name(line)
        return self._get_name(name, self._hero_dictionary)[0]

    def get_ability_hero(self, line):
        name = self._prepare_name(line)
        key, value = self._get_name(name, self._ability_dictionary)
        if key:
            return self._checkHurl(value['hurl'].lower())
        else:
            return None
