import unittest
from dotapatch.data import HeropediaData
import os.path as path


class TestDataFiles(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.DATA_DIR = HeropediaData.DATA_DIR

    def test_data_dir_exist(self):
        '''file: assert 'data' folder exists'''
        self.assertTrue(path.exists(self.DATA_DIR))

    def test_item_data_exist(self):
        '''file: assert 'itemdata' file exists'''
        ITEM_DATA = HeropediaData.ITEM_DATA
        self.assertTrue(path.isfile(path.join(
            self.DATA_DIR, ITEM_DATA)))

    def test_hero_data_exist(self):
        '''file: assert 'herodata' file exists'''
        HERO_DATA = HeropediaData.HERO_DATA
        self.assertTrue(path.isfile(path.join(
            self.DATA_DIR, HERO_DATA)))


class TestStringManipulation(unittest.TestCase):

    # sort
    def test_sort_hero_name_should_change(self):
        '''str: sort_hero("sHrEdDeR") returns "timbersaw"'''
        dictionary = ('sHrEdDeR', None)
        self.assertEqual('timbersaw', HeropediaData.sort_hero(dictionary))

    def test_sort_item_name_should_change(self):
        '''str: sort_item("sHrEdDeR") returns "timbersaw"'''
        dictionary = ('spHerE', None)
        self.assertEqual(
            "linken s sphere", HeropediaData.sort_item(dictionary))

    def test_sort_hero_name_should_not_change(self):
        '''str: sort("io") returns "io"'''
        dictionary = ('AsD', None)
        self.assertEqual('AsD', HeropediaData.sort_hero(dictionary))

    def test_sort_item_name_should_not_change(self):
        '''str: sort("io") returns "io"'''
        dictionary = ('AsD', None)
        self.assertEqual('AsD', HeropediaData.sort_item(dictionary))

    # prepare_d_name
    def test_prepare_d_name_should_change(self):
        '''str: prepare_d_name(nyx_line) returns nyx_dname'''
        nyx_line = 'NyX'
        nyx_dname = 'nyx assassin'
        self.assertEqual(
            nyx_dname, HeropediaData._prepare_d_name(nyx_line))

    def test_prepare_d_name_should_not_change(self):
        '''str: prepare_d_name(void_line) returns void_line.lower()'''
        void_line = 'FaCeLeSs VoId'
        self.assertEqual(
            void_line.lower(), HeropediaData._prepare_d_name(void_line))

    # prepare_item
    def test_prepare_item_should_change(self):
        '''
        str: prepare_item('dIfFuSaL_bLaDe_2') returns 'diffusal_blade'
        '''
        self.assertEqual(
            'diffusal_blade',
            HeropediaData._prepare_item('dIfFuSaL_bLaDe_2'))

    def test_prepare_item_should_not_change(self):
        '''str: prepare_item("DrAgOn_LaNcE") returns "dragon_lance"'''
        self.assertEqual(
            'dragon_lance',
            HeropediaData._prepare_item('DrAgOn_LaNcE'))


if __name__ == '__main__':
    unittest.main()
