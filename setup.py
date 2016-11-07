#!/usr/bin/env python3
# coding: utf-8
from setuptools import setup
import os.path as path


try:
    with open(path.abspath(path.join('dotapatch',
                                     'version.py'))) as version:
        exec(version.read())
except:
    print('ERROR version not found')
    __version__ = ''

try:
    with open('PyPIREADME.rst', 'r') as readme:
        info_long_description = readme.read()
except:
    try:
        print('PyPIREADME.rst not found, will use README.md instead')
        print('WARNING README.md should not be uploaded to PyPI')
        with open('README.md', 'r') as readme:
            info_long_description = readme.read()
    except:
        print('ERROR README.md not found either')
        info_long_description = ''


info_name = 'dotapatch'
info_url = 'https://github.com/arthurazs/{}/'.format(info_name)
info_download = '{}archive/v{}.tar.gz'.format(info_url, __version__)


setup(
    name=info_name,
    version=__version__,
    author='Arthur Zopellaro',
    author_email='arthurazsoares@gmail.com',
    description=('Parse Dota 2 text patches to html format.'),
    license='MIT',
    keywords=(
        'dota dota2 patch changelog html clean dotapatch convert'
    ),
    url=info_url,
    download_url=info_download,
    packages=['dotapatch'],
    package_data={
        'dotapatch': [
            'templates/*', 'data/*']},
    long_description=info_long_description,
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
        'Topic :: Games/Entertainment',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Interpreters',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    setup_requires=['setuptools', 'pip', 'nose', 'rednose'],
    install_requires=['requests'],
    entry_points={
        'console_scripts': [
            '{}=dotapatch.__main__:main'.format(info_name)]
    },
    tests_require=['nose', 'rednose', 'tox'],
    test_suite='nose.collector'
)
