import unittest
from dotapatch.data import HeropediaData


def setUpModule():
    global data
    data = HeropediaData()


class TestHeroDictionary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.hero = 'Juggernaut: base damage reduced by 2'

    def test_get_item_name_hero(self):
        '''hero: get_item_name(hero) returns None'''
        name = data.get_item_name(self.hero)
        self.assertIsNone(name)

    def test_get_hero_name_hero(self):
        '''hero: get_hero_name(hero) returns hero_id'''
        hero_id = 'juggernaut'
        name = data.get_hero_name(self.hero)
        self.assertEqual(hero_id, name)

    def test_get_hero_name_hero_new_structure(self):
        '''hero: get_hero_name("Nightstalker") returns "night_stalker"'''
        hero_id = 'night_stalker'
        name = data.get_hero_name('Nightstalker')
        self.assertEqual(hero_id, name)


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


class TestItemDictionary(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.item = 'Dragon Lance: strength reduced from 14 to 13'

    def test_get_item_name_item(self):
        '''item: get_item_name(item) returns item_id'''
        item_id = 'dragon_lance'
        name = data.get_item_name(self.item)
        self.assertEqual(item_id, name)

    def test_get_hero_name_item(self):
        '''item: get_hero_name(item) returns None'''
        name = data.get_hero_name(self.item)
        self.assertIsNone(name)


if __name__ == '__main__':
    unittest.main()
