# coding: utf-8
from setuptools import setup
import os.path as path


info_name = 'dotapatch'

try:
    with open(path.abspath(path.join(info_name, 'version.py'))) as version:
        exec(version.read())
except IOError as err:
    print(err)
    __version__ = ''

try:
    with open('PyPIREADME.rst', 'r') as readme:
        info_long_description = readme.read()
except IOError as err1:
    try:
        print('PyPIREADME.rst not found, will use README.md instead')
        print('WARNING README.md should not be uploaded to PyPI')
        with open('README.md', 'r') as readme:
            info_long_description = readme.read()
    except IOError as err2:
        print('ERROR README.md not found either')
        print()
        print(err1)
        print(err2)
        print()
        info_long_description = ''

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
    packages=[info_name, 'tests'],
    package_data={info_name: [
        'templates/*', 'data/*', 'changelogs/706f', 'changelogs/707d']},
    data_files=[(info_name, [
        'PyPIREADME.rst', 'requirements.txt', 'LICENSE', 'tox.ini',
        'CODE_OF_CONDUCT.md', 'CONTRIBUTING.md'])],
    long_description=info_long_description,
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
        'Programming Language :: Python :: 3.3',
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
            '{0} = {0}.__main__:main'.format(info_name)]
    },
    tests_require=['coverage>=4.4.2'],
    test_suite='nose.collector'
)
