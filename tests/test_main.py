'''Tests for __main__ methods'''
from unittest import TestCase, main as unit_main
from mock import patch
import os.path as path
from os import remove
from dotapatch.__main__ import get_parser, dotapatch
from dotapatch.patch import Dotapatch


class TestMain(TestCase):
    '''Tests main module'''

    def test_get_parser(self):
        '''main: assert get_parser() returns default values'''

        parser = get_parser()
        with patch('sys.argv', ['dotapatch', '706e', '707d']):
            args = parser.parse_args()

        changelog_list = args.changelogs
        template = args.template
        log_level = args.log_level
        save_log = args.save_log

        result = changelog_list == ['706e', '707d']
        result &= template == 'default'
        result &= log_level == 'INFO'
        result &= save_log is False

        self.assertTrue(result)

    def test_dotapatch(self):
        '''main: assert dotapatch() returns SUCCESS'''
        file_name = '706f'
        changelog = path.abspath(
            path.join('dotapatch', 'changelogs', file_name))
        status = dotapatch([changelog], 'default', None)
        remove(file_name + '.html')
        self.assertEqual(Dotapatch.SUCCESS, status)


if __name__ == '__main__':
    unit_main()
