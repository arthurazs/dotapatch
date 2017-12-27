'''Tests for __main__ methods'''
from unittest import TestCase, main as unit_main
from dotapatch.__main__ import get_args, main, DONT_PARSE


class TestMain(TestCase):
    '''Tests main module'''

    def test_get_args(self):
        '''main: assert get_args() returns default values'''
        _, template, log_level, save_log = get_args()
        result = template == 'default'
        result &= log_level == 'INFO'
        result &= save_log is False
        self.assertTrue(result)

    def test_main(self):
        '''main: assert main(False) returns DONT_PARSE'''
        with self.assertRaises(SystemExit) as context:
            main(False)
        self.assertEqual(DONT_PARSE, context.exception.code)


if __name__ == '__main__':
    unit_main()
