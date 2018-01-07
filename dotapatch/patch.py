# coding: utf-8
'''This is the main module the core of dotapatch.'''
from __future__ import print_function, absolute_import
import os.path as path
from collections import defaultdict
from logging import getLogger as get_logger
from dotapatch.model import Html
from dotapatch.data import HeropediaData


ERROR = -1
SUCCESS = 0
WARNING = 1

_LOGGER = get_logger('dotapatch.patch')


def _read_file(file_path):
    '''Reads the changelog file.

    Parameters
    ----------
    file_path : str
        Changelog to be parsed, it can either be ``filename`` or
        ``absolute_path/filename``

    Returns
    -------
    general : list[str]
        Dictionary of items to be added into the items section

    patch_version : str
        Patch version, e.g. ``7.07f``

    line_count : int
        Changelog lines read

    Raises
    ------
    exceptions.OSError
        Changelog file not found

    '''
    if not path.isfile(file_path):
        error_title = '{} not found'.format(file_path)
        raise OSError(error_title)

    with open(file_path, 'r') as changelog:
        general = []
        for line in changelog:
            line = line.replace('* ', '').rstrip()
            if line:
                general.append(line)

    patch_version = general[0].split(':')[0]
    general = general[2:]
    line_count = len(general)

    return general, patch_version, line_count


def _organize_heropedia(general):
    '''Searches for ``items`` and ``heroes`` lines.

    Parameters
    ----------
    general : list[str]
        List of general changelog lines to be added into the general section

    Returns
    -------
    items : dict
        Dictionary of items to be added into the items section

    heroes : dict
        Dictionary of heroes to be added into the heroes section

    Note
    ----
    Both ``dict`` use the following structure:
    ``{'dname': ['Change one.', 'Change two.']}``

    '''

    data = HeropediaData()

    # Organize changelog
    items = defaultdict(list)
    heroes = defaultdict(list)

    for line in general[:]:
        found_hero = data.get_hero_name(line)

        # Remove hero/item name, capitalize the line
        formatted_line = ' '.join(line.split(': ')[1:])
        formatted_line = formatted_line.capitalize()

        if found_hero:
            heroes[found_hero].append(formatted_line)
            general.remove(line)
        else:
            found_item = data.get_item_name(line)
            if found_item:
                items[found_item].append(formatted_line)
                general.remove(line)

    return items, heroes


def _generate_html(patch_version, template, general, items, heroes):
    '''Saves the parsed changelog lines as ``patch_name.html``.

    Note
    ----
    Both ``dict`` use the following structure:
    ``{'dname': ['Change one.', 'Change two.']}``

    Parameters
    ----------
    patch_version : str
        Patch version, e.g. ``7.07f``

    template : str
        Template to be used as base to parse the changelog, it can either be
        the ``name`` or ``absolute_path/name``

    general : list[str]
        List of general changelog lines to be added into the general section

    items : dict
        Dictionary of items to be added into the items section

    heroes : dict
        Dictionary of heroes to be added into the heroes section
    '''

    patch_name = patch_version.replace('.', '')

    with open(path.abspath(patch_name + '.html'), 'w') as text:
        model = Html(patch_version, template)
        model.add_general(general)
        model.add_items(items)
        model.add_heroes(heroes)
        model.close()
        print(model.get_content(), file=text)
        _LOGGER.info(
            'HTML saved at {}.html'
            .format(path.abspath(patch_name)))


def parse(file_path, template='default'):
    '''Parses the changelog.

    Parameters
    ----------
    file_path : str
        Changelog to be parsed, it can either be ``filename`` or
        ``absolute_path/filename``

    template : str
        Template to be used as base to parse the changelog, it can either be
        the ``name`` or ``absolute_path/name``

    Returns
    -------
    status : int
        Parsing status

    Note
    ----
        ``status == 0`` : Conversion went smoothly

        ``status  < 0`` : Critical error

        ``status >= 1`` : Some lines under GENERAL section should be reviewed
    '''
    status = ERROR

    general, patch_version, line_count = _read_file(file_path)

    _LOGGER.info('Parsing {}'.format(patch_version))

    items, heroes = _organize_heropedia(general)

    _generate_html(patch_version, template, general, items, heroes)

    # Feedback
    new_line_count = \
        sum(len(changes) for changes in heroes.values()) \
        + sum(len(changes) for changes in items.values())

    status = line_count - new_line_count

    if status == 0:
        _LOGGER.info(
            '{} conversion went smoothly.'.format(patch_version))
    elif status < 0:
        _LOGGER.critical('Contact me at @arthurazs')
    else:
        if status == 1:
            message = '''{} had 1 line under GENERAL updates:
* {}

This line might be a hero/item update and you should manually place it
at the proper location.'''.format(patch_version, ''.join(general))
            _LOGGER.warning(message)
        else:
            message = '{} had {} lines under GENERAL updates:' \
                .format(patch_version, str(status))
            for line in general:
                message = ('{}\n* {}'.format(message, line))
            message = '''{}

Some of these lines might be hero/item updates and you should manually
place them at the proper location.'''.format(message)
            _LOGGER.warning(message)

    return status
