#!/usr/bin/env python3
#coding: utf-8
import requests, ast, os.path, argparse
from collections import defaultdict
from model import Html

parser = argparse.ArgumentParser(description="This software formats a Dota2' changelog text into HTML.")
parser.add_argument('--file', '-f', action='store', help="changelog to be formated", required = True, dest = 'file')
parser.add_argument('--version', '-v', action='version', version='%(prog)s: 0.0v')
args = parser.parse_args()

#CONSTANTS
DATA = 'data/'
CHANGELOG = 'changelogs/'
ITEM_DATA = 'itemdata'
HERO_DATA = 'herodata'
ABILITY_DATA = 'abilitydata'

#Initialization Functions
def loadFile(name):
    link = 'http://www.dota2.com/jsfeed/heropediadata?feeds=' + name
    code = requests.get(link)
    data = code.text.replace('{"' + name + '":', '').replace('}}', '}').replace(':false', ':False').replace(':null', ':None').replace(':true', ':True')
    dictionary = ast.literal_eval(data)
    return dictionary

def openFile(name):
    with open(DATA + name, 'r') as text:
        data = text.read()
        dictionary = ast.literal_eval(data)
        return dictionary

def saveFile(name, content):
    with open(DATA + name, 'w') as text:
        print(content, file=text)

#Check folders
if not os.path.exists(DATA):
    os.makedirs(DATA)

if not os.path.exists(CHANGELOG):
    os.makedirs(CHANGELOG)

#Data Initialization
if(not os.path.isfile(DATA + ITEM_DATA)):
    item_dictionary = loadFile(ITEM_DATA)
    saveFile(ITEM_DATA, item_dictionary)
else:
    item_dictionary = openFile(ITEM_DATA)

if(not os.path.isfile(DATA + HERO_DATA)):
    hero_dictionary = loadFile(HERO_DATA)
    saveFile(HERO_DATA, hero_dictionary)
else:
    hero_dictionary = openFile(HERO_DATA)

if(not os.path.isfile(DATA + ABILITY_DATA)):
    ability_dictionary = loadFile(ABILITY_DATA)
    saveFile(ABILITY_DATA, ability_dictionary)
else:
    ability_dictionary = openFile(ABILITY_DATA)

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

    #Handle name bugs
    def checkDname(name):
        if (name.split()[0].lower() == 'drow'):
            return 'Drow Ranger'
        if (name.split()[0].lower() == 'nyx\'s'):
            return 'Nyx Assassin'
        elif (name.split()[0].lower() == 'smokescreen'):
            return 'Smoke Screen'
        elif (name.split()[0].lower() == 'starfall'):
            return 'Starstorm'
        return name

    def checkHurl(name):
        if (name.split()[0].lower() == 'io'):
            return 'wisp'
        if (name.split()[0].lower() == 'underlord'):
            return 'abyssal_underlord'
        return name

    #Default Function
    def get_name(name, dictionary):
        for key, value in dictionary.items():
            length = len(value['dname'].split(' '))
            if (checkDname(' '.join(name[:length])) == value['dname']):
                return (key, value)
        return (None, None)

    #Name Functions
    def get_item_name(name):
        return get_name(name, item_dictionary)[0]

    def get_hero_name(name):
        return get_name(name, hero_dictionary)[0]

    def get_ability_hero(name):
        key, value = get_name(name, ability_dictionary)
        if key:
            return checkHurl(value['hurl'].lower())
        else:
            return None

    #Organize changelog
    item = defaultdict(list)
    hero = defaultdict(list)
    ability = defaultdict(list)
    for line in lines[:]:
        names = line.split(' ')[:3]
        found_ability = get_ability_hero(names)
        if found_ability:
            ability[found_ability].append(line)
            lines.remove(line)

    for line in lines[:]:
        names = line.split(' ')[:3]
        found_hero = get_hero_name(names)
        if found_hero:
            hero[found_hero].append(line)
            lines.remove(line)
        else:
            found_item = get_item_name(names)
            if found_item:
                item[found_item].append(line)
                lines.remove(line)

    hero.update(ability)

    #Generate .html
    with open(simpleChangelogName + '.html', 'w') as text:
        model = Html(changelogName)
        model.addGeneral(lines)
        model.addItems(item)
        model.addHeros(hero)
        model.close()
        print(model.getContent(), file=text)

    status = len(lines)
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
    #TODO Implement a secondary list to show which lines require manual input

else:
    print ('''ERROR!
'{0}' not found.
Make sure {0} is inside the 'changelogs' folder.
Also check if the filename you typed is correct.

Contact me at @arthurazs if this error persists.'''.format(args.file))
