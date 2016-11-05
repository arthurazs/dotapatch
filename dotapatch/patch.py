#!/usr/bin/env python3
# coding: utf-8
from __future__ import print_function
from __future__ import absolute_import
import os.path as path
from collections import defaultdict
from .model import Html
from .data import HeropediaData


def main(filename, template='default'):
    file_path = path.abspath(filename)

    # Open changelog
    if path.isfile(file_path):
        with open(file_path, 'r') as changelog:
            # read changelog
            lines = []
            for line in changelog:
                lines.append(line.replace('* ', '').rstrip())
            patch_version = lines[0][:-1]
            patch_name = patch_version.replace('.', '')
            lines = lines[2:]
            initialLineCount = len(lines)

        data = HeropediaData()

        # Organize changelog
        item = defaultdict(list)
        hero = defaultdict(list)
        ability = defaultdict(list)

        for line in lines[:]:
            found_ability = data.get_ability_hero(line)
            if found_ability:
                ability[found_ability].append(line)
                lines.remove(line)

        for line in lines[:]:
            found_hero = data.get_hero_name(line)
            if found_hero:
                hero[found_hero].append(line)
                lines.remove(line)
            else:
                found_item = data.get_item_name(line)
                if found_item:
                    item[found_item].append(line)
                    lines.remove(line)

        # Merge ability into hero
        for key, value in ability.items():
            if(key in hero):
                hero[key].extend(ability[key])
            else:
                hero[key] = ability[key]

        # Generate .html
        with open(patch_name + '.html', 'w') as text:
            model = Html(patch_version, template)
            model.addGeneral(lines)
            model.addItems(item)
            model.addHeros(hero)
            model.close()
            print(model.getContent(), file=text)

        # Feedback
        currentLineCount = sum(len(changes) for changes in hero.values()) \
            + sum(len(changes) for changes in item.values())
        status = initialLineCount - currentLineCount
        if (status == 0):
            print('SUCCESS!\nConversion went smoothly.')
        elif (status < 0):
            print('CRITICAL ERROR!\nContact me at @arthurazs')
        else:
            print('WARNING!')
            if (status == 1):
                print('1 line under GENERAL updates:')
                print('* ' + ''.join(lines))
                print('\nThis line might be a hero/item update and you '
                      'should manually place it at the proper location.')
            else:
                print(str(status) + ' lines under GENERAL updates:')
                for line in lines:
                    print('* ' + line)
                print('\nSome of these lines might be hero/item updates'
                      ' and you should manually place them at the proper '
                      'location.')

    else:
        # ERROR
        print(
            '''ERROR {full} not found

In case {name} is in a directory other than
{path} try:

 1) 'cd' over to the correct directory
 2) run dotapatch again
 e.g.
     $ cd /whole/path/to/file/
     $ dotapatch {name}

 or

 1) run dotapatch specifying the /whole/path/to/file/{name}
 e.g.
     $ dotapatch /whole/path/to/file/{name}

Contact me at @arthurazs if the error persists.
            '''.format(
                full=file_path,
                path=path.dirname(file_path),
                name=path.basename(file_path)
            )
        )
