'''Tests for __main__ methods'''
from unittest import TestCase, main as unit_main
from mock import patch
import os.path as path
from os import remove  # , rename
from dotapatch.patch import SUCCESS
# from dotapatch.data import HeropediaData as data
from dotapatch.__main__ import get_parser, dotapatch, main


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
        status = dotapatch([changelog])
        remove(file_name + '.html')
        self.assertEqual(SUCCESS, status)

    def test_dotapatch_raises_oserror(self):
        '''main: assert dotapatch('non existent file') returns error'''
        status = dotapatch(['?'])
        self.assertEqual(-13, status)

    def test_main_changelog(self):
        '''main: assert main(changelog) exits with SUCCESS'''
        file_name = '706f'
        changelog = path.abspath(
            path.join('dotapatch', 'changelogs', file_name))
        with patch('sys.argv', ['dotapatch', changelog]):
            status = main(True)
        remove(file_name + '.html')
        self.assertEqual(SUCCESS, status)

    def test_main_no_changelog(self):
        '''main: assert main() returns SUCCESS'''
        with patch('sys.argv', ['dotapatch']):
            status = main(True)
        self.assertEqual(SUCCESS, status)

    # def test_update_data(self):
    #     '''main: assert dotapatch -u updates heropediadata'''

    #     hero_data = path.join(data.DATA_DIR, data.HERO_DATA)
    #     hero_backup = hero_data + '.backup'
    #     rename(hero_data, hero_backup)

    #     item_data = path.join(data.DATA_DIR, data.ITEM_DATA)
    #     item_backup = item_data + '.backup'
    #     rename(item_data, item_backup)

    #     with patch('sys.argv', ['dotapatch', '-u']):
    #         status = main(True)

    #     result = SUCCESS == status
    #     result &= path.isfile(hero_data)
    #     result &= path.isfile(item_data)

    #     rename(hero_backup, hero_data)
    #     rename(item_backup, item_data)

    #     self.assertTrue(result)


if __name__ == '__main__':
    unit_main()
