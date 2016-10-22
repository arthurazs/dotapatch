#!/usr/bin/env python3
#coding: utf-8
import requests, ast, os.path
from collections import defaultdict

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

#changelog = str(input('File name: ')) #TODO use input
changelog = '688e'
file = open('changelogs/'+changelog, 'r')

lines = []
for line in file:
    lines.append(line.replace('* ', '').rstrip())
    
def get_name(name, dictionary):
    for key, value in dictionary.items():
        length = len(value['dname'].split(' '))
        if (' '.join(name[:length]) in value['dname']):
            return (key, value)
    return (None, None)

def get_item_name(name):
    return get_name(name, item_dictionary)[0]

def get_hero_name(name):
    return get_name(name, hero_dictionary)[0]

def get_ability_hero(name):
    key, value = get_name(name, ability_dictionary)
    if key:
        return '_'.join(key.replace(value['dname'].lower().replace(' ', '_'), '').split('_')[:-1]) #TODO improve
    else:
        return None
    
item = {}
base = {}
ability = {}
for line in lines:
    names = line.split(' ')[:3]
    found_ability = get_ability_hero(names)
    if found_ability:
        ability[found_ability] = line
    
for line in lines:
    names = line.split(' ')[:3]
    found_hero = get_hero_name(names)
    if found_hero:
         base[found_hero] = line
    else:
        found_item = get_item_name(names)
        if found_item:
            item[found_item] = line

hero = base.copy()
hero.update(ability) #TODO put dic in order

#import re
#from collections import Counter
#c = Counter()
#c.copy(w.lower() for w in re.findall('[a-zA-Z]+', hero))
#print (c)
#print (item)
#print (hero)
#print (ability)
#print (hero_dictionary.items())
#print (get_skill_hero(['Arcane', '']))
file.close()
