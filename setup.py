# coding: utf-8
'''Setup for dotapatch.'''
from setuptools import setup
import os.path as path


APP_NAME = 'dotapatch'

try:
    with open(path.abspath(path.join(APP_NAME, 'version.py'))) as version:
        exec(version.read())
except IOError as err:
    print(err)
    __version__ = ''

try:
    with open('README.rst', 'r') as readme:
        APP_LONG_DESCRIPTION = readme.read()
except IOError as err:
    print('ERROR README.rst not found')
    print(err)
    APP_LONG_DESCRIPTION = ''

APP_URL = 'https://github.com/arthurazs/{}/'.format(APP_NAME)
APP_DOWNLOAD_URL = '{}archive/v{}.tar.gz'.format(APP_URL, __version__)


setup(
    name=APP_NAME,
    version=__version__,
    author='Arthur Zopellaro',
    author_email='arthurazsoares@gmail.com',
    description=('Parse Dota 2 text patches to html format.'),
    license='MIT',
    keywords=(
        'dota dota2 patch changelog html clean dotapatch convert'
    ),
    url=APP_URL,
    download_url=APP_DOWNLOAD_URL,
    packages=[APP_NAME, 'tests'],
    package_data={APP_NAME: [
        'templates/*', 'data/*', 'changelogs/706f', 'changelogs/707d']},
    data_files=[(APP_NAME, [
        'requirements.txt', 'LICENSE', 'tox.ini', 'CODE_OF_CONDUCT.rst',
        'CONTRIBUTING.rst', 'AUTHORS.rst'])],
    long_description=APP_LONG_DESCRIPTION,
    python_requires='>=2.7, <4',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    setup_requires=['nose>=1.3.7', 'rednose>=1.2.3'],
    entry_points={
        'console_scripts': [
            '{0} = {0}.__main__:main'.format(APP_NAME)]
    },
    tests_require=['coverage>=4.4.2', 'mock>=2.0.0'],
    test_suite='nose.collector'
)
