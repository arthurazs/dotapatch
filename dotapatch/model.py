'''Module for the HTML structure.'''
from __future__ import print_function, absolute_import
import os.path as path
from ast import literal_eval
from logging import getLogger as get_logger
from dotapatch.data import HeropediaData


class Html(object):
    '''Manages HTML output.'''

    TEMPLATES_DIR = path.abspath(
        path.join(path.dirname(__file__), 'templates'))

    def _load_template(self, template_name='default'):
        '''Loads given template.

        Note
        ----
        If ``template`` is not found, loads ``default`` template instead

        Parameters
        ----------
        template_name : str
            Template to be loaded, it can either be the ``name`` or
            ``absolute_path/template``

        Returns
        -------
        template_content : str
            Template content

        Raises
        ------
        exceptions.OSError
            Default template not found (py3)
        exceptions.IOError
            Default template not found (py2)
        '''
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

    @classmethod
    def _check_template_missing_keys(cls, dictionary):
        '''Checks if the loaded template is complete.

        Parameters
        ----------
        dictionary : dict
            Template's dictionary to be evaluated

        Returns
        -------
        missing_keys : list[str]
            List of missing keys
        '''
        necessary_keys = [
            'OPEN_HTML', 'OPEN_GENERAL', 'OPEN_GENERAL_UL',
            'GENERAL_LI', 'CLOSE_GENERAL_UL', 'CLOSE_GENERAL',
            'OPEN_ITEMS', 'OPEN_ITEMS_UL', 'ITEMS_LI',
            'CLOSE_ITEMS_UL', 'CLOSE_ITEMS', 'OPEN_HEROES',
            'OPEN_HEROES_UL', 'HEROES_LI', 'CLOSE_HEROES_UL',
            'CLOSE_HEROES', 'CLOSE_HTML']
        missing_keys = []
        for item in necessary_keys:
            if item not in dictionary.keys():
                missing_keys.append(item)
        return missing_keys

    def _eval_template(self, template_content):
        '''Parses the template's content into dict.

        Parameters
        ----------
        template_content : str
            Template's content to be parsed

        Returns
        -------
        template_dictionary : dict
            Parsed template

        Raises
        ------
        exceptions.SyntaxError
            If the are any missing keys or if the template isn't a dict
        '''
        try:
            template_dictionary = literal_eval(template_content)
            if isinstance(template_dictionary, dict):
                missing_keys = Html._check_template_missing_keys(
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
        '''Logger helper.

        Prints a critical message and exits.

        Warning
        -------
        TODO Remove SystemExit(-1)

        Parameters
        ----------
        msg : str
            Error description

        err : exceptions
            Raised exception

        Raises
        ------
        exceptions.SystemExit
            Exits the application with ``-1``
        '''
        self.logger.error(
            msg)
        self.logger.critical(
            '{}: {}'.format(err.__class__.__name__, err))
        raise SystemExit(-1)

    def _read_template(self, template_name='default'):
        '''Loads given template and parses its content into dict.

        Note
        ----
        If ``template`` is not found, loads ``default`` template instead

        Parameters
        ----------
        template_name : str
            Template to be loaded, it can either be the ``name`` or
            ``absolute_path/template``

        Returns
        -------
        template_dictionary : dict
            Parsed template
        '''
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
        '''Initializes Html output manager and loads the template.

        Parameters
        ----------
        title : str
            HTML Title
        template : str
            Template to be loaded, it can either be the ``name`` or
            ``absolute_path/template``
        '''
        self.logger = get_logger('dotapatch.model')
        self._title = title

        if template != 'default':
            self.logger.info("{} using '{}' template.".format(title, template))

        self._template_dictionary = self._read_template(template)

        self._bg_style = False
        self._content = self._template_dictionary['OPEN_HTML'] \
            .format(title=self._title)

    def _add_content(self, text):
        '''Append content to the HTML.

        Parameters
        ----------
        text : str
            Text to be appended
        '''
        self._content = self._content + text

    def add_general(self, lines):
        '''Add lines to general section.

        Parameters
        ----------
        lines : list[str]
            List of general changelog lines to be added into the general
            section
        '''
        if lines:
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
        '''Add item_dictionary to items section.

        Note
        ----
        ``{'dname': ['Change one.', 'Change two.']}``

        Parameters
        ----------
        item_dictionary : dict
            Dictionary of items to be added into the items section
        '''
        if item_dictionary:
            self._add_content(
                self._template_dictionary['OPEN_ITEMS']
                .format(style=int(self._bg_style)))

            for key, values in sorted(item_dictionary.items(),
                                      key=HeropediaData.sort_item):
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
        '''Add hero_dictionary to heroes section.

        Note
        ----
        ``{'dname': ['Change one.', 'Change two.']}``

        Parameters
        ----------
        hero_dictionary : dict
            Dictionary of heroes to be added into the heroes section
        '''
        if hero_dictionary:
            self._add_content(
                self._template_dictionary['OPEN_HEROES']
                .format(style=int(self._bg_style)))

            for key, values in sorted(hero_dictionary.items(),
                                      key=HeropediaData.sort_hero):
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
        '''Closes the HTML tags.

        .. warning::
            Must be called once!'''
        self._add_content(self._template_dictionary['CLOSE_HTML'])

    # Returns HTML Content
    def get_content(self):
        '''Returns the whole HTML content.

        Returns
        -------
        content : str
            Whole HTML content'''
        return self._content

    def get_dictionary_value(self, section):
        '''Returns the content for the given section.

        Parameters
        ----------
        section : str
            The content section to be accessed, e.g. ``OPEN_GENERAL``

        Returns
        -------
        content : str
            Section content'''
        content = self._template_dictionary[section]
        return content
