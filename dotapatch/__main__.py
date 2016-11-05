from __future__ import absolute_import
import sys
import argparse
from .version import __version__
from .patch import main


parser = argparse.ArgumentParser(
    prog='dota2patches', description='This software formats a Dota2 '
    'changelog text into HTML.')
parser.add_argument(
    'file', action='store', help='changelog to be formated')
parser.add_argument(
    '--template', '-t', action='store', dest='template',
    default='default', help='base template to generate HTML')
parser.add_argument(
    '--version', '-V', action='version',
    version='%(prog)s: v{}'
    .format(__version__))

args = parser.parse_args()

sys.exit(main(args.file, args.template))
