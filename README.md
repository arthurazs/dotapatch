# Dota 2: Changelog formatted as it should.

| Platform |                                                                                                                                                                                                                                                                                                                                       Status                                                                                                                                                                                                                                                                                                                                        |
|:--------:|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|  GitHub  | [![GitHub Release](https://img.shields.io/github/release/arthurazs/dotapatch.svg)](https://github.com/arthurazs/dotapatch/releases) [![GitHub Tag](https://img.shields.io/github/tag/arthurazs/dotapatch.svg)](https://github.com/arthurazs/dotapatch/tags) [![GitHub License](https://img.shields.io/github/license/arthurazs/dotapatch.svg)](https://github.com/arthurazs/dotapatch/blob/master/LICENSE) [![GitHub Issues](https://img.shields.io/github/issues/arthurazs/dotapatch.svg)](https://github.com/arthurazs/dotapatch/issues) [![GitHub Pull Requests](https://img.shields.io/github/issues-pr/arthurazs/dotapatch.svg)](https://github.com/arthurazs/dotapatch/pulls) |
|   PyPI   | [![PyPI Version](https://img.shields.io/pypi/v/dotapatch.svg)](https://pypi.python.org/pypi/dotapatch) [![PyPI License](https://img.shields.io/pypi/l/dotapatch.svg)](https://pypi.python.org/pypi/dotapatch) [![Python Version](https://img.shields.io/pypi/pyversions/dotapatch.svg)](https://pypi.python.org/pypi/dotapatch) [![PyPI Wheel](https://img.shields.io/pypi/wheel/dotapatch.svg)](https://pypi.python.org/pypi/dotapatch) [![PyPI Status](https://img.shields.io/pypi/status/dotapatch.svg)](https://pypi.python.org/pypi/dotapatch) |
|  Status  | [![CircleCI](https://img.shields.io/circleci/project/github/arthurazs/dotapatch.svg)](https://circleci.com/gh/arthurazs/dotapatch) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/f92dab093ac0404fa76deb1b1ce23ea2)](https://www.codacy.com/app/arthurazsoares/dota2patches?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=arthurazs/dota2patches&amp;utm_campaign=Badge_Grade) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/f92dab093ac0404fa76deb1b1ce23ea2)](https://www.codacy.com/app/arthurazsoares/dota2patches?utm_source=github.com&utm_medium=referral&utm_content=arthurazs/dota2patches&utm_campaign=Badge_Coverage) [![codecov](https://codecov.io/gh/arthurazs/dotapatch/branch/master/graph/badge.svg)](https://codecov.io/gh/arthurazs/dotapatch) |

**dotapatch** is a software which aims the automation of formatting `simple text changelog` into `clear html changelog`.

Check the [Gameplay Update 7.07d](https://arthurazs.github.io/dotapatch/707d.html). This is the latest patch parsed using **dotapatch**.

**Contents**

- [Too long; didn't read](#tldr)
- [Getting started](#getting-started)
    - [How does it work](#how-does-it-work)
- [Using dotapatch](#using-dotapatch)
    - [Installing dotapatch](#installing-dotapatch)
    - [Gathering a new changelog](#gathering-a-new-changelog)
    - [Running dotapatch](#running-dotapatch)
    - [Testing dotapatch](#testing-dotapatch)
- [Built with](#built-with)
- [Authors](#authors)
- [Task list](#task-list)
- [Contributing](#contributing)
- [Code of Conduct](#code-of-conduct)
- [License](#license)

## TL;DR

    $ pip install dotapatch

Save a changelog file in accordance with the following format:

    7.07d:
    ==
    * Nullifier: Manacost reduced from 100 to 75
    * Alchemist: Unstable Concoction damage increased from 150/220/290/360 to 160/240/320/400

Head over to the directory you saved the changelog and run **dotapatch**.

    $ cd Desktop/changelogs
    $ dotapatch 707d
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/707d.html
    INFO Conversion went smoothly.

Make sure that `<filename>` is in your current directory. You can also provide the `path` to the changelog.

    $ dotapatch /home/arthurazs/Desktop/changelogs/707d
    INFO HTML saved at /home/arthurazs/707d.html
    INFO Conversion went smoothly.

## Getting started
You will need python.

    $ sudo apt-get install python

### How does it work

    $ dotapatch -h
    usage: dotapatch [-h] [-t TEMPLATE] [-V] [-d] [-s] [-q] file

    Parse Dota 2 text patches to html format.

    positional arguments:
      file                  changelog to be formated

    optional arguments:
      -h, --help            show this help message and exit
      -t TEMPLATE, --template TEMPLATE
                            base template to generate HTML
      -V, --version         show program's version number and exit

    logging arguments:
      -d, --debug           set verbosity level to DEBUG
      -s, --save-log        save log output
      -q, --quiet           less verbose

Run **dotapatch** stating the full path to the file:

    $ dotapatch /home/arthurazs/Desktop/changelogs/707d
    INFO HTML saved at /home/arthurazs/707d.html
    INFO Conversion went smoothly.

Or you can head over to the directory with the changelog and run **dotapatch** stating only the filename:

    $ cd Desktop/changelogs
    $ dotapatch 707d
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/707d.html
    INFO Conversion went smoothly.

There are some optional arguments that you can use:

    $ dotapatch --version
    dotapatch: v2.0

    $ dotapatch 707d
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/707d.html
    INFO Conversion went smoothly.

    $ dotapatch 707d --quiet

    $ dotapatch 707d --debug
    DEBUG Reading changelog.
    DEBUG Parsing changelog.
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/707d.html
    INFO Conversion went smoothly.

    $ dotapatch dotapatch/changelogs/707d --save-log
    INFO Recording log file at /home/arthurazs/git/dotapatch/dotapatch.log
    INFO HTML saved at /home/arthurazs/git/dotapatch/707d.html
    INFO Conversion went smoothly.

    $ dotapatch dotapatch/changelogs/707d --template gh-pages
    INFO Using 'gh-pages' template.
    INFO HTML saved at /home/arthurazs/git/dotapatch/707d.html
    INFO Conversion went smoothly.

- `--template` indicates which template is going to be used to parse the changelog. The `default` template generates a standalone HTML that uses [dota2](http://dota2.com) css files.
- `--debug` and `--quiet` increase and decrease **dotapatch**'s verbosity, respectively.
- `--save-log` saves a log with maximum verbosity output.

## Using dotapatch

### Installing dotapatch

Install **dotapatch** using `pip`:

    $ pip install dotapatch

Or [clone (or download)](https://help.github.com/articles/cloning-a-repository/) this [repository](/../../), head over to the folder and install using the `setup.py`:

    $ git clone https://github.com/arthurazs/dotapatch.git
    $ cd dotapatch
    $ python setup.py install

**OPTIONALLY** You can use **dotapatch** without installing. Just [clone (or download)](https://help.github.com/articles/cloning-a-repository/) the [repository](/../../).

    $ git clone https://github.com/arthurazs/dotapatch.git

### Gathering a new changelog

- Go to [dota2 news](https://www.dota2.com/news/updates/) page and locate the latest **patch**.
- Copy and save it as a file.
    - The content you save **must** start with the patch name followed by colon (e.g. `7.07d:`).
    - The second line won't be read, so you can leave it with anything other than a real changelog line (e.g. `--`).
    - **All** the following lines **must** start with a star/asterisk (e.g. `* Anti-mage magic resistance reduced by a lot`).

    ```
    7.07d:
    ==
    * Necronomicon: Mana Break damage from 60 to 50%
    * Nullifier: Cooldown reduced from 14 to 13
    * Nullifier: Manacost reduced from 100 to 75

    * Alchemist: Unstable Concoction damage increased from 150/220/290/360 to 160/240/320/400
    * Bane: Enfeeble duration reduced from 20 to 14/16/18/20
    * Bane: Brain Sap damage rescaled from 90/160/230/300 to 75/150/225/300
    ```

### Running dotapatch

If you've installed **dotapatch**, head over to the folder where you saved the changelog file and run **dotapatch**.

    $ cd Desktop/changelogs
    $ dotapatch 707d
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/707d.html
    INFO Conversion went smoothly.

If you haven't installed **dotapatch**, head over to the **dotapatch** folder and run **dotapatch** as a **module**.

    $ cd Desktop/dotapatch
    $ python -m dotapatch /home/arthurazs/Desktop/changelogs/707d
    INFO HTML saved at /home/arthurazs/Desktop/dotapatch/707d.html
    INFO Conversion went smoothly.

### Testing dotapatch

You will need `tox`:

    $ pip install tox

[Clone (or download)](https://help.github.com/articles/cloning-a-repository/) this [repository](/../../), head over to the folder and run `tox`:

    $ git clone https://github.com/arthurazs/dotapatch.git
    $ cd dotapatch
    $ tox

## Built with

**dotapatch** uses the following libraries:

 - [ast](https://docs.python.org/3.4/library/ast.html)
     - Transforms data from HeropediaData into dictionary
 - [os.path](https://docs.python.org/3.4/library/os.path.html)
     - Makes sure all directories are created and all data are downloaded
 - [argparse](https://docs.python.org/3.4/library/argparse.html)
     - Enables the use of arguments. Try `$ ./patch.py -h`
 - collections.[defaultdict](https://docs.python.org/3.4/library/collections.html#collections.defaultdict)
     - defaultdict(list) stores each line of the changelog inside a list (inside a dictionary)
     - Each `dictionary.keys()` (hero) stores `dictionary.values()` (hero changes)
     - `dictionary.values()` returns a list with all changes
 - [requests](https://github.com/kennethreitz/requests)
     - Fetches HeropediaData files
 - [logging](https://docs.python.org/3.4/library/logging.html)
     - Manage *dotapatch* logs
 - [tox](https://tox.readthedocs.io)
     - Run tests for Python 2.7 and Python 3.4
         - [unittest](https://docs.python.org/3.4/library/unittest.html)
             - Base for the tests
             - [nose](http://nose.readthedocs.io/en/latest/) test suite (nosetests)
                 - [--rednose](https://github.com/JBKahn/rednose) plugging which improves readability
 - [pip](https://pypi.python.org/pypi)
     - Installation manager
     - [setuptools](https://github.com/pypa/setuptools)
         - Setup manager

## Authors
- [**Arthur Zopellaro**](https://github.com/arthurazs)
    - *Creator*

## Task list

 - **TODO** see [projects](/../../projects).
 - **Changelog** see [releases](/../../releases).

## Contributing

Do you have any feedback, questions or ideias? Do you want to report a bug?
Even better, would you like to fix a bug or implement a feature?

First of all, thank you! Make sure to read the
[Contributing Guidelines][contributing] for details.

## Code of Conduct

The [Code of Conduct] for this project is based on
[Contributor Covenant][conduct]. Any unacceptable behavior may be reported by
contacting the project team at [arthurazsoares@gmail.com][email].

## License
This project is licensed under the [MIT License](LICENSE).

[conduct]:          https://www.contributor-covenant.org

[email]:            mailto:arthurazsoares@gmail.com
[Code of Conduct]:  https://github.com/arthurazs/dotapatch/blob/master/CODE_OF_CONDUCT.md
[contributing]:     https://github.com/arthurazs/dotapatch/blob/master/CONTRIBUTING.md
