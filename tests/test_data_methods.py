from unittest import TestCase, main as unit_main
from dotapatch.data import HeropediaData


def setUpModule():
    global data
    data = HeropediaData()


def tearDownModule():
    global data
    del data


class TestHeroDictionary(TestCase):

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


class TestGeneralDictionary(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.general = 'Illusions attack damage reduction against buildings'

    def test_get_item_name_general(self):
        '''general: get_item_name(general) returns None'''
        name = data.get_item_name(self.general)
        self.assertIsNone(name)

    def test_get_hero_name_general(self):
        '''general: get_hero_name(general) returns None'''
        name = data.get_hero_name(self.general)
        self.assertIsNone(name)


class TestItemDictionary(TestCase):

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
    unit_main()
