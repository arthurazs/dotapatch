'''Tests for Dotapatch functions'''
from unittest import TestCase, main as unit_main
import os.path as path
from os import remove
from dotapatch.patch import parse, SUCCESS, WARNING


class Test(TestCase):
    '''Tests changelog parsing'''

    @classmethod
    def setUpClass(cls):
        '''Sets up changelog path'''
        cls.file_path = path.abspath(path.join('dotapatch', 'changelogs'))

    def test_raises_ioerror(self):
        '''ptc: parse invalid file and return -1 (or less)'''
        file_path = path.abspath('?')
        self.assertRaises(OSError, parse, file_path)

    def test_dont_raise_ioerror(self):
        '''ptc: parse file with no GENERAL section and return 0'''
        file_name = '706f'

        result = parse(path.join(self.file_path, file_name))
        remove(file_name + '.html')
        self.assertEqual(SUCCESS, result)

    def test_parse(self):
        '''
        ptc: parse file with GENERAL section and return 1 (or greater)
        '''
        file_name = '707d'

        result = parse(path.join(self.file_path, file_name))
        remove(file_name + '.html')
        self.assertLessEqual(WARNING, result)


if __name__ == '__main__':
    unit_main()
