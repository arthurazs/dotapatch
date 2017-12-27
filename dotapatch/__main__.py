'''dotapatch's entry point'''
from __future__ import absolute_import
from sys import exit as sys_exit
import os.path as path
from argparse import ArgumentParser
from logging import DEBUG, StreamHandler, Formatter, FileHandler
from logging import getLogger as get_logger, getLevelName as get_level
from dotapatch.version import __version__
from dotapatch.patch import Dotapatch


def get_parser():
    '''Creates dotapatch's arguments.

    Returns
    -------
    parser : ArgumentParser
        Parser with all arguments.
    '''
    parser = ArgumentParser(
        prog='dotapatch', description='Parses Dota 2 text patches to html'
        ' format.')
    parser.add_argument(
        'changelog', action='store', help='changelog to be formated',
        metavar='changelog_file', nargs='?', default=None)
    parser.add_argument(
        '-t', '--template', action='store', dest='template',
        default='default', help='base template to generate HTML',
        metavar='template_file')
    parser.add_argument(
        '-V', '--version', action='version',
        version='%(prog)s: v{}'
        .format(__version__))
    log_group = parser.add_argument_group('logging arguments')
    log_group.add_argument(
        '-d', '--debug', help='set verbosity level to DEBUG',
        action='store_const', dest='log_level',
        const='DEBUG', default='INFO')
    log_group.add_argument(
        '-s', '--save-log', help='save log output',
        action='store_true', dest='save_log')
    log_group.add_argument(
        '-q', '--quiet', help='less verbose',
        action='store_const', dest='log_level',
        const='ERROR')

    return parser


def main(changelog, template='default', log_level='INFO', save_log=False):
    '''dotapatch's entry point.

    Get the arguments, initializes logging, parses the changelog.

    Parameters
    ----------
    changelog : str
        Changelog to be parsed.
        It can be either the filename or the absolute_filepath/filename.

    template : str (optional, 'default')
        Template to be loaded.
        It can be either the template name or the absolute_path/template.

    log_level : str (optional, 'INFO')
        Log level to be outputed.
        Every level equal or higher will be printed.

    save_log : bool (optional, False)
        Whether the log should be saved into a file or not.

    Returns
    -------
    status : int
        Parsing status.
    '''

    if log_level:
        logger = get_logger('dotapatch')
        logger.setLevel(DEBUG)

        stream_handler = StreamHandler()
        stream_handler.setLevel(get_level(log_level))
        stream_formatter = Formatter('%(levelname)s %(message)s')
        stream_handler.setFormatter(stream_formatter)
        logger.addHandler(stream_handler)

        if save_log:
            file_handler = FileHandler('dotapatch.log', 'w')
            file_handler.setLevel(DEBUG)
            file_formatter = Formatter('''
        %(asctime)s (%(name)s, line %(lineno)d)
        %(levelname)s %(message)s''')
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)
            logger.info('Recording log file at {}'.format(
                path.abspath('dotapatch.log')))

    return Dotapatch(changelog, template).parse()


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    changelog = args.changelog
    template = args.template
    log_level = args.log_level
    save_log = args.save_log
    if changelog:
        status = main(changelog, template, log_level, save_log)
        sys_exit(status)
    else:
        parser.print_help()
