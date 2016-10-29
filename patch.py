#!/usr/bin/env python3
#coding: utf-8
from __future__ import print_function
import os.path, argparse
from collections import defaultdict
from model import Html
from data import HeropediaData

parser = argparse.ArgumentParser(description="This software formats a Dota2' changelog text into HTML.")
parser.add_argument('--file', '-f', action='store', help="changelog to be formated", required = True, dest = 'file')
parser.add_argument('--theme', '-t', action='store', help="theme to be used", default = 'default', dest = 'theme')
parser.add_argument('--version', '-v', action='version', version='%(prog)s: v1.0 (Yasha)')
args = parser.parse_args()

#CONSTANT
CHANGELOG = 'changelogs/'

#Checks if the line starts with fixed and removes it
def getName(value):
    names = value.split(' ')
    if names[0].lower() == 'fixed':
        name = names[1:]
    else:
        name = names[:]
    return name

#Check changelog folder
if not os.path.exists(CHANGELOG):
    os.makedirs(CHANGELOG)

#Open changelog
if os.path.isfile(CHANGELOG+args.file):
    with open(CHANGELOG+args.file, 'r') as changelog:

        #Read changelog
        lines = []
        for line in changelog:
            lines.append(line.replace('* ', '').rstrip())
        changelogName = lines[0][:-1]
        simpleChangelogName = changelogName.replace('.', '')
        lines = lines[2:]
        initialLineCount = len(lines)

    data = HeropediaData()

    #Organize changelog
    item = defaultdict(list)
    hero = defaultdict(list)
    ability = defaultdict(list)

    for line in lines[:]:
        name = getName(line)
        found_ability = data.get_ability_hero(name)
        if found_ability:
            ability[found_ability].append(line)
            lines.remove(line)

    for line in lines[:]:
        name = getName(line)
        found_hero = data.get_hero_name(name)
        if found_hero:
            hero[found_hero].append(line)
            lines.remove(line)
        else:
            found_item = data.get_item_name(name)
            if found_item:
                item[found_item].append(line)
                lines.remove(line)

    #Merge ability into hero
    for key, value in ability.items():
        if(key in hero):
            hero[key].extend(ability[key])
        else:
            hero[key] = ability[key]

    #Generate .html
    with open(simpleChangelogName + '.html', 'w') as text:
        model = Html(changelogName, args.theme)
        model.addGeneral(lines)
        model.addItems(item)
        model.addHeros(hero)
        model.close()
        print(model.getContent(), file=text)

    #Feedback
    currentLineCount = sum(len(changes) for changes in hero.values()) + sum(len(changes) for changes in item.values())
    status = initialLineCount - currentLineCount
    if (status == 0):
        print('SUCCESS!\nConversion went smoothly.')
    elif (status < 0):
        print('CRITICAL ERROR!\nContact me at @arthurazs')
    else:
        print('WARNING!')
        if (status == 1):
            print('1 line under GENERAL updates:')
            print('* ' + ' '.join(lines))
            print('\nThis line might be a hero/item update and you should manually place it at the proper location.')
        else:
            print(str(status) + ' lines under GENERAL updates:')
            for line in lines:
                print('* ' + line)
            print('\nSome of these lines might be hero/item updates and you should manually place them at the proper location.')

else:
    #ERROR
    print ('''ERROR!
'{0}' not found.
Make sure {0} is inside the 'changelogs' folder.
Also check if the filename you typed is correct.

Contact me at @arthurazs if this error persists.'''.format(args.file))
