'''Tests for Html functions'''
from unittest import TestCase, main as unit_main
from dotapatch.model import Html
import os.path as path
from os import remove


class TestTemplateFile(TestCase):
    '''Tests template file'''

    def test_template_dir_exist(self):
        '''tmpl: assert 'templates' folder exists'''
        self.assertTrue(path.exists(Html.TEMPLATES_DIR))

    def test_use_default_template(self):
        '''tmpl: try nonexistent template and use default instead'''
        try:
            Html('test', '?123asd,v03ekca0cd0')
        except (IOError, OSError, SyntaxError, ValueError, SystemExit) as err:
            self.fail('Raised {}.'.format(err.__class__.__name__))

    def test_malformed_template(self):
        '''tmpl: raise error for malformed template'''
        file_path = path.join(Html.TEMPLATES_DIR, 'test_delete')
        with self.assertRaises(SystemExit) as context:  # TODO Is this correct?
            with open(file_path, 'w') as test_delete:
                test_delete.write('{1:2}')
            Html('test', 'test_delete')
        remove(file_path)
        self.assertEqual(context.exception.code, -1)


class TestHtmlDictionary(TestCase):
    '''Tests Html dictionary'''

    @classmethod
    def setUpClass(cls):
        '''Sets up Html base'''
        cls.html = Html('test')
        cls.desired_content = \
            cls.html.get_dictionary_value('OPEN_HTML') \
            .format(title='test')
        cls.bg_style = False

    def tearDown(self):
        '''Resets content and style'''
        TestHtmlDictionary.desired_content = self.desired_content
        TestHtmlDictionary.bg_style = self.bg_style

    def test_add_general(self):
        '''html: assert general content is added properly'''
        lines = ['content one', 'content two']
        self.html.add_general(lines)
        self.desired_content += \
            self.html.get_dictionary_value('OPEN_GENERAL') \
                .format(style=int(self.bg_style)) + \
            self.html.get_dictionary_value('OPEN_GENERAL_UL') + \
            self.html.get_dictionary_value('GENERAL_LI') \
                .format(line=lines[0]) + \
            self.html.get_dictionary_value('GENERAL_LI') \
                .format(line=lines[1]) + \
            self.html.get_dictionary_value('CLOSE_GENERAL_UL') + \
            self.html.get_dictionary_value('CLOSE_GENERAL')
        self.bg_style = not self.bg_style

        self.assertEqual(
            self.desired_content, self.html.get_content())

    def test_add_items(self):
        '''html: assert item content is added properly'''
        key = 'dname'
        values = ['Change one.', 'Change two.']
        items = {key: values}
        self.html.add_items(items)

        self.desired_content += \
            self.html.get_dictionary_value('OPEN_ITEMS') \
                .format(style=int(self.bg_style)) + \
            self.html.get_dictionary_value('OPEN_ITEMS_UL') \
                .format(key=key) + \
            self.html.get_dictionary_value('ITEMS_LI') \
                .format(value=values[0]) + \
            self.html.get_dictionary_value('ITEMS_LI') \
                .format(value=values[1]) + \
            self.html.get_dictionary_value('CLOSE_ITEMS_UL') + \
            self.html.get_dictionary_value('CLOSE_ITEMS')
        self.bg_style = not self.bg_style

        self.assertEqual(
            self.desired_content, self.html.get_content())

    def test_add_heroes(self):
        '''html: assert hero content is added properly'''
        key = 'dname'
        values = ['Change one.', 'Change two.']
        heroes = {key: values}
        self.html.add_heroes(heroes)

        self.desired_content += \
            self.html.get_dictionary_value('OPEN_HEROES') \
                .format(style=int(self.bg_style)) + \
            self.html.get_dictionary_value('OPEN_HEROES_UL') \
                .format(key=key) + \
            self.html.get_dictionary_value('HEROES_LI') \
                .format(value=values[0]) + \
            self.html.get_dictionary_value('HEROES_LI') \
                .format(value=values[1]) + \
            self.html.get_dictionary_value('CLOSE_HEROES_UL') + \
            self.html.get_dictionary_value('CLOSE_HEROES')
        self.bg_style = not self.bg_style

        self.assertEqual(
            self.desired_content, self.html.get_content())

    def test_close(self):
        '''html: assert content closes properly'''
        self.html.close()

        self.desired_content += \
            self.html.get_dictionary_value('CLOSE_HTML')

        self.assertEqual(
            self.desired_content, self.html.get_content())


if __name__ == '__main__':
    unit_main()
