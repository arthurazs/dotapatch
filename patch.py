#!/usr/bin/env python3
#coding: utf-8
import requests, ast, os.path

item_link = "http://www.dota2.com/jsfeed/heropediadata?feeds=itemdata"
try:
    item_code = requests.get(item_link)
except requests.exceptions.RequestException as e:  #FIXME try: if can, save and use it; if cant, use the saved one and print "not up to date"
    print (e)
    sys.exit(1)
item_data = item_code.text.replace('{"itemdata":', '').replace('}}', '}').replace(':false', ':False').replace(':null', ':None').replace(':true', ':True')
item_dictionary = ast.literal_eval(item_data)

hero_link = "http://www.dota2.com/jsfeed/heropediadata?feeds=herodata"
hero_code = requests.get(hero_link)
hero_data = hero_code.text.replace('{"herodata":', '').replace('}}', '}').replace(':false', ':False').replace(':null', ':None').replace(':true', ':True')
hero_dictionary = ast.literal_eval(hero_data)

ability_link = "http://www.dota2.com/jsfeed/heropediadata?feeds=abilitydata"
ability_code = requests.get(ability_link)
ability_data = ability_code.text.replace('{"abilitydata":', '').replace('}}', '}').replace(':false', ':False').replace(':null', ':None').replace(':true', ':True')
ability_dictionary = ast.literal_eval(ability_data)

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
