from setuptools import setup
import os.path as path

try:
    with open(path.abspath(path.join('dotapatch',
                                     'version.py'))) as version:
        exec(version.read())
except:
    print('ERROR version not found')
    __version__ = ''

setup(
    name="dotapatch",
    version=__version__,
    author="Arthur Zopellaro",
    author_email="arthurazsoares@gmail.com",
    description=('Parse dota 2 text patches to html format.'),
    license="MIT",
    keywords="dota dota2 patch changelog html clean",
    url="https://github.com/arthurazs/dota2patches",
    packages=['dotapatch'],
    package_data={
        'dotapatch': [
            'templates/default', 'templates/dota2',
            'data/abilitydata', 'data/herodata', 'data/itemdata']},
    long_description='',
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
    setup_requires=['setuptools', 'nose', 'rednose'],
    install_requires=['requests'],
    entry_points={
        'console_scripts': ['dotapatch=dotapatch.__main__:main']
    },
    tests_require=['nose', 'rednose'],
    test_suite="nose.collector",
)
