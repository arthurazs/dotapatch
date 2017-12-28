'''Tests for HeropediaData functions'''
from unittest import TestCase, main as unit_main
from dotapatch.data import HeropediaData
import os.path as path


class TestDataFiles(TestCase):
    '''Test if files/folders exists'''

    @classmethod
    def setUpClass(cls):
        '''Sets up directory to check'''
        cls.DATA_DIR = HeropediaData.DATA_DIR

    def test_data_dir_exist(self):
        '''file: assert 'data' folder exists'''
        self.assertTrue(path.exists(self.DATA_DIR))

    def test_item_data_exist(self):
        '''file: assert 'itemdata' file exists'''
        item_data = HeropediaData.ITEM_DATA
        self.assertTrue(path.isfile(path.join(self.DATA_DIR, item_data)))

    def test_hero_data_exist(self):
        '''file: assert 'herodata' file exists'''
        hero_data = HeropediaData.HERO_DATA
        self.assertTrue(path.isfile(path.join(self.DATA_DIR, hero_data)))


class TestStringManipulation(TestCase):
    '''Tests string manipulation'''

    def test_sort_hero_name_change(self):
        '''str: sort_hero("wisp") returns "io"'''
        dictionary = ('wisp', None)
        self.assertEqual('io', HeropediaData.sort_hero(dictionary))

    def test_sort_item_name_change(self):
        '''str: sort_item("sphere") returns "linken s sphere"'''
        dictionary = ('sphere', None)
        self.assertEqual(
            "linken s sphere", HeropediaData.sort_item(dictionary))

    def test_sort_hero_name_not_change(self):
        '''str: sort("io") returns "io"'''
        dictionary = ('io', None)
        self.assertEqual('io', HeropediaData.sort_hero(dictionary))

    def test_sort_item_name_not_change(self):
        '''str: sort("linken s sphere") returns "linken s sphere"'''
        dictionary = ('linken s sphere', None)
        self.assertEqual(
            'linken s sphere', HeropediaData.sort_item(dictionary))


if __name__ == '__main__':
    unit_main()
