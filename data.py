import requests, ast, os.path
class HeropediaData (object):

    #CONSTANTS
    DATA = 'data/'
    ITEM_DATA = 'itemdata'
    HERO_DATA = 'herodata'
    ABILITY_DATA = 'abilitydata'

    #Initialization Functions
    def _loadFile(self, name):
        link = 'http://www.dota2.com/jsfeed/heropediadata?feeds=' + name
        code = requests.get(link)
        data = code.text.replace('{"' + name + '":', '').replace('}}', '}').replace(':false', ':False').replace(':null', ':None').replace(':true', ':True')
        dictionary = ast.literal_eval(data)
        return dictionary

    def _openFile(self, name):
        with open(self.DATA + name, 'r') as text:
            data = text.read()
            dictionary = ast.literal_eval(data)
            return dictionary

    def _saveFile(self, name, content):
        with open(self.DATA + name, 'w') as text:
            print(content, file=text)

    #Initialization
    def __init__(self):
        #Check data folder
        if not os.path.exists(self.DATA):
            os.makedirs(self.DATA)

        #Data Initialization
        if(not os.path.isfile(self.DATA + self.ITEM_DATA)):
            self._item_dictionary = self._loadFile(self.ITEM_DATA)
            self._saveFile(self.ITEM_DATA, self._item_dictionary)
        else:
            self._item_dictionary = self._openFile(self.ITEM_DATA)

        if(not os.path.isfile(self.DATA + self.HERO_DATA)):
            self._hero_dictionary = self._loadFile(self.HERO_DATA)
            self._saveFile(self.HERO_DATA, self._hero_dictionary)
        else:
            self._hero_dictionary = self._openFile(self.HERO_DATA)

        if(not os.path.isfile(self.DATA + self.ABILITY_DATA)):
            self._ability_dictionary = self._loadFile(self.ABILITY_DATA)
            self._saveFile(self.ABILITY_DATA, self._ability_dictionary)
        else:
            self._ability_dictionary = self._openFile(self.ABILITY_DATA)

    def getDictionary(self, name):
        if name == 'ability':
            return self._ability_dictionary
        elif name == 'hero':
            return self._hero_dictionary
        elif name == 'item':
            return self._item_dictionary
        else:
            return None

    @staticmethod
    def sort(dictionary):
        name = dictionary[0]
        if (name.lower() == 'wisp'):
            return 'io'
        if (name.lower() == 'abyssal_underlord'):
            return 'underlord'
        return name

    #Handle name bugs
    def _checkDname(self, name):
        if (name.split()[0].lower() == 'drow'):
            return 'Drow Ranger'
        if (name.split()[0].lower() == 'nyx\'s'):
            return 'Nyx Assassin'
        elif (name.split()[0].lower() == 'smokescreen'):
            return 'Smoke Screen'
        elif (name.split()[0].lower() == 'starfall'):
            return 'Starstorm'
        return name

    def _checkHurl(self, name):
        if (name.split()[0].lower() == 'io'):
            return 'wisp'
        if (name.split()[0].lower() == 'underlord'):
            return 'abyssal_underlord'
        return name

    def _checkItem(self, name):
        if (name.lower() == 'diffusal_blade_2'):
            return 'diffusal_blade'
        return name

    #Default Function
    def _get_name(self, name, dictionary):
        for key, value in dictionary.items():
            length = len(value['dname'].split(' '))
            if (self._checkDname(' '.join(name[:length])) == value['dname']):
                return (self._checkItem(key), value)
        return (None, None)

    #Name Functions
    def get_item_name(self, name):
        return self._get_name(name, self._item_dictionary)[0]

    def get_hero_name(self, name):
        return self._get_name(name, self._hero_dictionary)[0]

    def get_ability_hero(self, name):
        key, value = self._get_name(name, self._ability_dictionary)
        if key:
            return self._checkHurl(value['hurl'].lower())
        else:
            return None
