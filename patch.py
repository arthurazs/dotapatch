#!/usr/bin/env python3
#coding: utf-8
import requests, ast, os.path
from collections import defaultdict
from model import Html

#CONSTANTS
DATA = 'data/'
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
#changelog = str(input('File name: ')) #TODO use input
changelogFile = '688e'
file = open('changelogs/'+changelogFile, 'r')

#Read changelog
lines = []
for line in file:
    lines.append(line.replace('* ', '').rstrip())
changelogName = lines[0][:-1]
simpleChangelogName = changelogName.replace('.', '')
lines = lines[2:]

#Handle name bugs
def checkDname(name):
    if (name.split()[0].lower() == 'drow'):
        return 'Drow Ranger'
    elif (name.split()[0].lower() == 'smokescreen'):
        return 'Smoke Screen'
    return name

def checkHurl(name):
    if (name.split()[0].lower() == 'io'):
        return 'wisp'
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
for line in lines:
    names = line.split(' ')[:3]
    found_ability = get_ability_hero(names)
    if found_ability:
        ability[found_ability].append(line)

for line in lines:
    names = line.split(' ')[:3]
    found_hero = get_hero_name(names)
    if found_hero:
         hero[found_hero].append(line)
    else:
        found_item = get_item_name(names)
        if found_item:
            item[found_item].append(line)

base = hero.copy()
base.update(ability)

#Generate .html
with open(simpleChangelogName + '.html', 'w') as text:
    model = Html(changelogName)
    model.addHero(base)
    model.close()
    print(model.getContent(), file=text)

status = len(lines) - sum(len(changes) for changes in base.values()) - sum(len(changes) for changes in item.values())
if (status == 0):
    print ('Conversion went smoothly.')
elif (status < 0):
    print ('CRITICAL ERROR! Contact me at @arthurazs')
else:
    if (status == 1):
        print ('1 line requires manual input.')
    else:
        print (str(status) + ' lines require manual input.')
#TODO Implement a secondary list to show which lines require manual input
file.close()
