from __future__ import print_function
from __future__ import absolute_import
from .data import HeropediaData
import ast
import os.path as path


class Html (object):

    TEMPLATES_DIR = path.abspath(
        path.join(path.dirname(__file__), 'templates'))

    @staticmethod
    def _read_template(template_name):
        with open(path.join(Html.TEMPLATES_DIR, template_name), 'r') \
                as template_file:
            template_dictionary = ast.literal_eval(template_file.read())
        return template_dictionary

    # Initialization
    def __init__(self, title, template='default'):
        self._title = title
        self._template_dictionary = Html._read_template(template)
        self._bg_style = False
        self._content = self._template_dictionary['OPEN_HTML'] \
            .format(title=self._title)

    def _add_content(self, text):
        '''Append content to self._content

        Parameters
        ----------
        text : str
            Text to be appended.
        '''
        self._content = self._content + text

    def add_general(self, lines):
        '''Add [lines] to general section.

    Parameters
    ----------
    lines : list
        List of changelog lines to be added into the general section.
        '''
        if(lines):
            self._add_content(
                self._template_dictionary['OPEN_GENERAL']
                .format(style=int(self._bg_style)))
            self._add_content(
                self._template_dictionary['OPEN_GENERAL_UL'])

            for line in lines:
                self._add_content(
                    self._template_dictionary['GENERAL_LI']
                    .format(line=line))

            self._add_content(
                self._template_dictionary['CLOSE_GENERAL_UL'])
            self._add_content(self._template_dictionary['CLOSE_GENERAL'])
            self._bg_style = not self._bg_style

    def add_items(self, item_dictionary):
        '''Add {item_dictionary} to items section.

    Parameters
    ----------
    item_dictionary : dict
        {'dname': ['Change one.', 'Change two.']}
        Dictionary of items to be added into the items section.
        '''
        if(item_dictionary):
            self._add_content(
                self._template_dictionary['OPEN_ITEMS']
                .format(style=int(self._bg_style)))

            for key, values in sorted(item_dictionary.items()):
                self._add_content(
                    self._template_dictionary['OPEN_ITEMS_UL']
                    .format(key=key))
                for value in values:
                    self._add_content(
                        self._template_dictionary['ITEMS_LI']
                        .format(value=value))
                self._add_content(
                    self._template_dictionary['CLOSE_ITEMS_UL'])

            self._add_content(self._template_dictionary['CLOSE_ITEMS'])
            self._bg_style = not self._bg_style

    # Add HERO Contents
    def add_heroes(self, hero_dictionary):
        '''Add {hero_dictionary} to heroes section.

    Parameters
    ----------
    hero_dictionary : dict
        {'dname': ['Change one.', 'Change two.']}
        Dictionary of heroes to be added into the heroes section.
        '''
        if(hero_dictionary):
            self._add_content(
                self._template_dictionary['OPEN_HEROES']
                .format(style=int(self._bg_style)))

            for key, values in sorted(hero_dictionary.items(),
                                      key=HeropediaData.sort):
                self._add_content(
                    self._template_dictionary['OPEN_HEROES_UL']
                    .format(key=key))
                for value in values:
                    self._add_content(
                        self._template_dictionary['HEROES_LI']
                        .format(value=value))
                self._add_content(
                    self._template_dictionary['CLOSE_HEROES_UL'])

            self._add_content(self._template_dictionary['CLOSE_HEROES'])
            self._bg_style = not self._bg_style

    # Closes the HTML
    def close(self):
        self._add_content(self._template_dictionary['CLOSE_HTML'])

    # Returns HTML Content
    def get_content(self):
        return self._content

    def get_dictionary_value(self, key):
        return self._template_dictionary[key]
