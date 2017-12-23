import unittest
from dotapatch.patch import Dotapatch
import os.path as path


class Test(unittest.TestCase):

    def test_raises_ioerror(self):
        '''ptc: parse invalid file and return -1 (or less)'''
        file_path = path.abspath('?')
        dotapatch = Dotapatch(file_path)
        self.assertGreaterEqual(Dotapatch.ERROR, dotapatch.parse())

    def test_dont_raise_ioerror(self):
        '''ptc: parse file with no GENERAL section and return 0'''
        file_path = path.abspath(
            path.join('dotapatch', 'changelogs', '000a'))
        dotapatch = Dotapatch(file_path)
        self.assertEqual(Dotapatch.SUCCESS, dotapatch.parse())

    def test_parse(self):
        '''
        ptc: parse file with GENERAL section and return 1 (or greater)
        '''
        file_path = path.abspath(
            path.join('dotapatch', 'changelogs', '707d'))
        dotapatch = Dotapatch(file_path)
        self.assertLessEqual(Dotapatch.WARNING, dotapatch.parse())


if __name__ == '__main__':
    unittest.main()
