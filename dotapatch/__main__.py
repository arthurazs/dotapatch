from __future__ import absolute_import
import sys
import argparse
from .version import __version__
from .patch import Dotapatch
import logging
from logging import getLevelName as get_level
import os.path as path

parser = argparse.ArgumentParser(
    prog='dotapatch', description='Parse Dota 2 text patches to html'
    ' format.')
parser.add_argument(
    'file', action='store', help='changelog to be formated')
parser.add_argument(
    '-t', '--template', action='store', dest='template',
    default='default', help='base template to generate HTML')
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

args = parser.parse_args()


logger = logging.getLogger('dotapatch')
logger.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(get_level(args.log_level))
stream_formatter = logging.Formatter('%(levelname)s %(message)s')
stream_handler.setFormatter(stream_formatter)
logger.addHandler(stream_handler)

if args.save_log:
    file_handler = logging.FileHandler('dotapatch.log', 'w')
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('''
%(asctime)s (%(name)s, line %(lineno)d)
%(levelname)s %(message)s''')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    logger.info('Recording log file at {}'.format(
        path.abspath('dotapatch.log')))

dotapatch = Dotapatch(args.file, args.template)

sys.exit(dotapatch.parse())
