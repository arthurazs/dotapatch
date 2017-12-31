'''dotapatch's entry point'''
from __future__ import absolute_import
import os.path as path
from argparse import ArgumentParser
from logging import DEBUG, StreamHandler, Formatter, FileHandler
from logging import getLogger as get_logger, getLevelName as get_level
from dotapatch.version import __version__
from dotapatch.patch import parse
from dotapatch.data import HeropediaData


def get_parser():
    '''Creates app's arguments.

    Returns
    -------
    parser : ArgumentParser
        Parser with all arguments.
    '''
    parser = ArgumentParser(
        prog='dotapatch', description='Parses Dota 2 text patches to html'
        ' format.')
    parser.add_argument(
        'changelogs', action='store', help='changelog to be formated',
        metavar='changelog_file', nargs='*', default=None)
    parser.add_argument(
        '-t', '--template', action='store', dest='template',
        default='default', help='base template to generate HTML',
        metavar='template_file')
    parser.add_argument(
        '-u', '--update-data', action='store_true', dest='update',
        help='force heropediadata update')
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


def dotapatch(
        changelogs, template='default', update=False):
    '''Dotapatch's core.

    Get the arguments, initializes logging, parses the changelogs.

    Parameters
    ----------
    changelogs : list
        Changelog to be parsed.
        It can be either the filename or the absolute_filepath/filename.

    template : str (optional, 'default')
        Template to be loaded.
        It can be either the template name or the absolute_path/template.

    update : bool (optional, False)
        Whether heropedia's data should be updated or not.

    Returns
    -------
    status : int
        Parsing status.
    '''

    if update:
        HeropediaData.download_file(HeropediaData.ITEM_DATA)
        HeropediaData.download_file(HeropediaData.HERO_DATA)

    status = 0

    if changelogs:
        for filename in changelogs:
            try:
                status += parse(filename, template)
            except OSError as err:
                filename = path.abspath(filename)
                logger = get_logger('dotapatch')
                logger.error('{}: {}'.format(err.__class__.__name__, err))

                error_body = '''In case {name} is in a directory other than:
{path}

Try:

 1) 'cd' over to the correct directory
 2) run dotapatch again
 e.g.
     $ cd /whole/path/to/file/
     $ dotapatch {name}

 or

 1) run dotapatch specifying the /whole/path/to/file/{name}
 e.g.
     $ dotapatch /whole/path/to/file/{name}

Contact me at @arthurazs if the error persists.'''.format(
                    path=path.dirname(filename),
                    name=path.basename(filename))
                logger.warning(error_body)
                status = -13

    return status


def main(testing=False):
    '''main method.

    Calls get_parser(). If 'changelogs' is empty and 'update' is False,
    prints app usage. Otherwise calls dotapatch().

    Parameters
    ----------
    testing : bool (optional, False)
        Whether main is being called for testing or not.

    Returns
    -------
    status : int
        Parsing status.
    '''
    parser = get_parser()

    args = parser.parse_args()
    changelogs = args.changelogs
    template = args.template
    if testing:
        log_level = None
    else:
        log_level = args.log_level
    save_log = args.save_log
    update = args.update

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
            file_formatter = Formatter(
                '%(asctime)s (%(name)s, line %(lineno)d)\n'
                '%(levelname)s %(message)s\n')
            file_handler.setFormatter(file_formatter)
            logger.addHandler(file_handler)
            logger.info('Recording log file at {}'.format(
                path.abspath('dotapatch.log')))

    if changelogs or update:
        status = dotapatch(changelogs, template, update)
        return status
    else:
        parser.print_usage()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
