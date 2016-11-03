import unittest
from parser.data import HeropediaData


def setUpModule():
    global data
    data = HeropediaData()


class TestHeroDictionary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hero = 'Juggernaut base damage reduced by 2'

    def test_get_item_name_hero(self):
        '''hero: get_item_name(hero) returns None'''
        name = data.get_item_name(self.hero)
        self.assertIsNone(name)

    def test_get_hero_name_hero(self):
        '''hero: get_hero_name(hero) returns hero_id'''
        hero_id = 'juggernaut'
        name = data.get_hero_name(self.hero)
        self.assertEqual(hero_id, name)

    def test_get_ability_name_hero(self):
        '''hero: get_ability_hero(hero) returns None'''
        name = data.get_ability_hero(self.hero)
        self.assertIsNone(name)


class TestAbilityDictionary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ability = 'Shadow Poison initial damage reduced from 50 to '
        '26/34/42/50'

    def test_get_item_name_ability(self):
        '''ability: get_item_name(ability) returns None'''
        name = data.get_item_name(self.ability)
        self.assertIsNone(name)

    def test_get_hero_name_ability(self):
        '''ability: get_hero_name(ability) returns None'''
        name = data.get_hero_name(self.ability)
        self.assertIsNone(name)

    def test_get_ability_name_ability(self):
        '''ability: get_ability_hero(ability) returns ability_hero_id'''
        ability_hero_id = 'shadow_demon'
        name = data.get_ability_hero(self.ability)
        self.assertEqual(ability_hero_id, name)


class TestGeneralDictionary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.general = 'Illusions attack damage reduction against '
        'buildings increased from 25% to 30%'

    def test_get_item_name_general(self):
        '''general: get_item_name(general) returns None'''
        name = data.get_item_name(self.general)
        self.assertIsNone(name)

    def test_get_hero_name_general(self):
        '''general: get_hero_name(general) returns None'''
        name = data.get_hero_name(self.general)
        self.assertIsNone(name)

    def test_get_ability_name_general(self):
        '''general: get_ability_hero(general) returns None'''
        name = data.get_ability_hero(self.general)
        self.assertIsNone(name)


class TestItemDictionary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.item = 'Dragon Lance strength reduced from 14 to 13'

    def test_get_item_name_item(self):
        '''item: get_item_name(item) returns item_id'''
        item_id = 'dragon_lance'
        name = data.get_item_name(self.item)
        self.assertEqual(item_id, name)

    def test_get_hero_name_item(self):
        '''item: get_hero_name(item) returns None'''
        name = data.get_hero_name(self.item)
        self.assertIsNone(name)

    def test_get_ability_name_item(self):
        '''item: get_ability_hero(item) returns None'''
        name = data.get_ability_hero(self.item)
        self.assertIsNone(name)


if __name__ == '__main__':
    unittest.main()
