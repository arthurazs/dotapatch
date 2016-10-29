from __future__ import print_function
from data import HeropediaData
import ast

class Html (object):

    _THEMES_FOLDER = 'themes/'

    def _read_theme(self, theme_name):
        with open(self._THEMES_FOLDER + theme_name, 'r') as theme_file:
            theme_dictionary = ast.literal_eval(theme_file.read())
        return theme_dictionary

    #Initialization
    def __init__(self, title, theme = 'default'):
        self._title = title
        self._theme_dictionary = self._read_theme(theme)
        self._bgStyle = False
        self._content = self._theme_dictionary['OPEN_HTML'].format(title = self._title)

    #Default function for adding content
    def _addContent(self, text):
        self._content = self._content + text

    #Add GENERAL Contents
    def addGeneral(self, lines):
        if(lines):
            self._addContent(self._theme_dictionary['OPEN_GENERAL'].format(int(self._bgStyle)))
            self._addContent(self._theme_dictionary['OPEN_GENERAL_UL'])

            for line in lines:
                self._addContent(self._theme_dictionary['GENEREAL_LI'].format(line))

            self._addContent(self._theme_dictionary['CLOSE_GENERAL_UL'])
            self._addContent(self._theme_dictionary['CLOSE_GENERAL'])
            self._bgStyle = not self._bgStyle

    #Add ITEMS Contents
    def addItems(self, dictionary):
        if(dictionary):
            self._addContent(self._theme_dictionary['OPEN_ITEMS'].format(int(self._bgStyle)))

            for key, values in sorted(dictionary.items()):
                self._addContent(self._theme_dictionary['OPEN_ITEMS_UL'].format(key))
                for value in values:
                    self._addContent(self._theme_dictionary['ITEMS_LI'].format(value))
                self._addContent(self._theme_dictionary['CLOSE_ITEMS_UL'])

            self._addContent(self._theme_dictionary['CLOSE_ITEMS'])
            self._bgStyle = not self._bgStyle

    #Add HERO Contents
    def addHeros(self, dictionary):
        if(dictionary):
            self._addContent(self._theme_dictionary['OPEN_HEROES'].format(style = int(self._bgStyle)))

            for key, values in sorted(dictionary.items(), key=HeropediaData.sort):
                self._addContent(self._theme_dictionary['OPEN_HEROES_UL'].format(key = key))
                for value in values:
                    self._addContent(self._theme_dictionary['HEROES_LI'].format(value = value))
                self._addContent(self._theme_dictionary['CLOSE_HEROES_UL'])

            self._addContent(self._theme_dictionary['CLOSE_HEROES'])
            self._bgStyle = not self._bgStyle

    #Closes the HTML
    def close(self):
        self._addContent(self._theme_dictionary['CLOSE_HTML'])

    #Returns HTML Content
    def getContent(self):
        return self._content
