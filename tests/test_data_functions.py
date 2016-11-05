import unittest
from dotapatch.data import HeropediaData
import os.path as path


class TestDataFiles(unittest.TestCase):

    def setUp(self):
        self.DATA_DIR = HeropediaData.DATA_DIR

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

    def test_ability_data_exist(self):
        '''file: assert 'abilitydata' file exists'''
        ABILITY_DATA = HeropediaData.ABILITY_DATA
        self.assertTrue(path.isfile(path.join(
            self.DATA_DIR, ABILITY_DATA)))


class TestStringManipulation(unittest.TestCase):

    # sort
    def test_sort_name_should_change(self):
        '''str: sort("sHrEdDeR") returns "timbersaw"'''
        dictionary = ('sHrEdDeR', None)
        self.assertEqual('timbersaw', HeropediaData.sort(dictionary))

    def test_sort_name_should_not_change(self):
        '''str: sort("io") returns "io"'''
        dictionary = ('io', None)
        self.assertEqual('io', HeropediaData.sort(dictionary))

    # prepare_line
    def test_prepare_line_change(self):
        '''str: prepare_line("fIxEd something") returns "something"'''
        centaur = 'fIxEd Return working on Centaur Illusions'
        expected_result = 'Return working on Centaur Illusions'.split()
        actual_result = HeropediaData._prepare_line(centaur)
        self.assertEqual(expected_result, actual_result)

    def test_prepare_line_dont_change(self):
        '''str: prepare_line('something') returns 'something'.
        '''
        centaur = 'Return working on Centaur Illusions'
        expected_result = 'Return working on Centaur Illusions'.split()
        actual_result = HeropediaData._prepare_line(centaur)
        self.assertEqual(expected_result, actual_result)

    # prepare_d_name
    def test_prepare_d_name_should_change(self):
        '''str: prepare_d_name([nyx_line]) returns nyx_dname'''
        nyx_line = "NyX's Scepter Burrow cast time increased from "
        "1 to 1.5"
        nyx_dname = 'nyx assassin'
        line_list = nyx_line.split()
        self.assertEqual(
            nyx_dname, HeropediaData._prepare_d_name(line_list))

    def test_prepare_d_name_should_not_change(self):
        '''str: prepare_d_name([void_line]) returns void_line.lower()'''
        void_line = "FaCeLeSs VoId BaSe ArMoR rEdUcEd By 1"
        line_list = void_line.split()
        self.assertEqual(
            void_line.lower(), HeropediaData._prepare_d_name(line_list))

    # prepare_h_url
    def test_prepare_h_url_should_change(self):
        '''str: prepare_h_url("iO") returns "wisp"'''
        self.assertEqual(
            'wisp', HeropediaData._prepare_h_url('iO'))

    def test_prepare_h_url_should_not_change(self):
        '''str: prepare_h_url("RiKi") returns "riki"'''
        self.assertEqual(
            'riki', HeropediaData._prepare_h_url('RiKi'))

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

    # prepare_ability
    def test_prepare_ability_return_d_hero(self):
        '''str: prepare_ability(centaur) returns "centaur_warrunner"'''
        centaur = 'FiXeD rEtUrN working on Centaur Illusions'.split()
        self.assertEqual(
            'centaur_warrunner',
            HeropediaData._prepare_ability(centaur))

    def test_prepare_ability_return_None(self):
        '''str: prepare_ability(['laguna blade']) returns None'''
        self.assertEqual(
            None,
            HeropediaData._prepare_ability(['laguna blade']))


if __name__ == '__main__':
    unittest.main()
