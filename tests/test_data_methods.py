'''Tests for HeropediaData methods'''
from unittest import TestCase, main as unit_main
from dotapatch.data import HeropediaData


DATA = HeropediaData()


class TestHeroDictionary(TestCase):
    '''Tests hero dictionary'''

    @classmethod
    def setUpClass(cls):
        '''Sets up hero changelog line'''
        cls.hero = 'Juggernaut: base damage reduced by 2'

    def test_get_item_name_hero(self):
        '''hero: get_item_name(hero) returns None'''
        name = DATA.get_item_name(self.hero)
        self.assertIsNone(name)

    def test_get_hero_name_hero(self):
        '''hero: get_hero_name(hero) returns hero_id'''
        hero_id = 'juggernaut'
        name = DATA.get_hero_name(self.hero)
        self.assertEqual(hero_id, name)


class TestGeneralDictionary(TestCase):
    '''Tests general change (no item/hero change)'''

    @classmethod
    def setUpClass(cls):
        '''Sets up general changelog line'''
        cls.general = 'Illusions attack damage reduction against buildings'

    def test_get_item_name_general(self):
        '''general: get_item_name(general) returns None'''
        name = DATA.get_item_name(self.general)
        self.assertIsNone(name)

    def test_get_hero_name_general(self):
        '''general: get_hero_name(general) returns None'''
        name = DATA.get_hero_name(self.general)
        self.assertIsNone(name)


class TestItemDictionary(TestCase):
    '''Tests item dictionary'''

    @classmethod
    def setUpClass(cls):
        '''Sets up item changelog line'''
        cls.item = 'Dragon Lance: strength reduced from 14 to 13'

    def test_get_item_name_item(self):
        '''item: get_item_name(item) returns item_id'''
        item_id = 'dragon_lance'
        name = DATA.get_item_name(self.item)
        self.assertEqual(item_id, name)

    def test_get_hero_name_item(self):
        '''item: get_hero_name(item) returns None'''
        name = DATA.get_hero_name(self.item)
        self.assertIsNone(name)


class TestDictionaryManipulation(TestCase):
    '''Tests dictionary manipulation'''

    def test_download_file_fail(self):
        '''dwnl: assert 'file:///' can't be used '''
        with self.assertRaises(SystemExit) as context:  # TODO Is this correct?
            DATA.download_file('file:///')
        self.assertEqual(context.exception.code, -1)


if __name__ == '__main__':
    unit_main()
