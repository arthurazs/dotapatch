from __future__ import print_function
from __future__ import absolute_import
from .data import HeropediaData
import ast
import os.path as path
import logging


class Html (object):

    TEMPLATES_DIR = path.abspath(
        path.join(path.dirname(__file__), 'templates'))

    def _load_template(self, template_name='default'):
        try:
            with open(path.join(
                    Html.TEMPLATES_DIR, template_name), 'r') \
                    as template_file:
                template_content = template_file.read()
        except (IOError, OSError) as err:
            self.logger.warning(
                "'{}' template not found."
                .format(template_name))
            if template_name == 'default':
                raise err
            else:
                self.logger.warning("Using 'default' template instead.")
                template_content = self._load_template('default')
        return template_content

    def _check_template_missing_keys(self, dic):
        necessary_keys = [
            'OPEN_HTML', 'OPEN_GENERAL', 'OPEN_GENERAL_UL',
            'GENERAL_LI', 'CLOSE_GENERAL_UL', 'CLOSE_GENERAL',
            'OPEN_ITEMS', 'OPEN_ITEMS_UL', 'ITEMS_LI',
            'CLOSE_ITEMS_UL', 'CLOSE_ITEMS', 'OPEN_HEROES',
            'OPEN_HEROES_UL', 'HEROES_LI', 'CLOSE_HEROES_UL',
            'CLOSE_HEROES', 'CLOSE_HTML']
        missing_keys = []
        for item in necessary_keys:
            if item not in dic.keys():
                missing_keys.append(item)
        return missing_keys

    def _eval_template(self, template_content):
        try:
            template_dictionary = ast.literal_eval(template_content)
            if isinstance(template_dictionary, dict):
                missing_keys = self._check_template_missing_keys(
                    template_dictionary)
                if missing_keys:
                    raise SyntaxError(
                        'Necessary key not found in the template '
                        'dictionary: {}'.format(missing_keys))
            else:
                raise SyntaxError('Template is not a dictionary.')
        except (ValueError, SyntaxError) as err:
            self.logger.warning('Template file malformed.')
            self.logger.debug(
                'Template content ({}):\n{}'
                .format(err.__class__.__name__, template_content))
            raise err
        else:
            return template_dictionary

    def _critical(self, msg, err):
        self.logger.error(
            msg)
        self.logger.critical(
            '{}: {}'.format(err.__class__.__name__, err))
        raise SystemExit(-1)

    def _read_template(self, template_name='default'):
        template_dictionary = ''
        try:
            template_content = self._load_template(template_name)
            template_dictionary = self._eval_template(template_content)
        except (IOError, OSError) as err1:
            self._critical(
                'Impossible to continue without a template.',
                err1)
        except (ValueError, SyntaxError) as err2:
            self._critical(
                'Impossible to parse the template file to dictionary.',
                err2)
        return template_dictionary

    # Initialization
    def __init__(self, title, template='default'):
        self.logger = logging.getLogger('dotapatch.model')
        self._title = title

        if template != 'default':
            self.logger.info("Using '{}' template.".format(template))

        self._template_dictionary = self._read_template(template)

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
