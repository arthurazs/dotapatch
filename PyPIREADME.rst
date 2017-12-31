Dota 2: Changelog formatted as it should.
=========================================

+---+------------------------------------------------------------------------+
| P | Status                                                                 |
| l |                                                                        |
| a |                                                                        |
| t |                                                                        |
| f |                                                                        |
| o |                                                                        |
| r |                                                                        |
| m |                                                                        |
+===+========================================================================+
| G | |GitHub Release| |GitHub Tag| |GitHub License| |GitHub Issues| |GitHub |
| i | Pull Requests|                                                         |
| t |                                                                        |
| H |                                                                        |
| u |                                                                        |
| b |                                                                        |
+---+------------------------------------------------------------------------+
| P | |PyPI Version| |PyPI License| |Python Version| |PyPI Wheel| |PyPI      |
| y | Status|                                                                |
| P |                                                                        |
| I |                                                                        |
+---+------------------------------------------------------------------------+
| H | |CircleCI| |Codacy Badge| |Codacy Badge| |codecov|                     |
| e |                                                                        |
| a |                                                                        |
| l |                                                                        |
| t |                                                                        |
| h |                                                                        |
+---+------------------------------------------------------------------------+

**dotapatch** is a software which aims the automation of formatting
``simple text changelog`` into ``clear html changelog``.

Check the `Gameplay Update
7.07d <https://arthurazs.github.io/dotapatch/707d.html>`__. This is the
latest patch parsed using **dotapatch**.

**Contents**

-  `Too long; didn't read <#tldr>`__
-  `Getting started <#getting-started>`__

   -  `How does it work <#how-does-it-work>`__

-  `Using dotapatch <#using-dotapatch>`__

   -  `Installing dotapatch <#installing-dotapatch>`__
   -  `Gathering a new changelog <#gathering-a-new-changelog>`__
   -  `Running dotapatch <#running-dotapatch>`__
   -  `Testing dotapatch <#testing-dotapatch>`__

      -  `tox <#tox>`__
      -  `nosetests <#nosetests>`__

-  `Built with <#built-with>`__
-  `Authors <#authors>`__
-  `Task list <#task-list>`__
-  `Contributing <#contributing>`__
-  `Code of Conduct <#code-of-conduct>`__
-  `License <#license>`__

TL;DR
-----

::

    $ pip install dotapatch

Save a changelog file in accordance with the following format:

::

    7.07d:
    ==
    * Nullifier: Manacost reduced from 100 to 75
    * Alchemist: Unstable Concoction damage increased from 150/220/290/360 to 160/240/320/400

Head over to the directory you saved the changelog and run
**dotapatch**.

::

    $ cd changelogs
    $ dotapatch 706f 707d
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/changelogs/706f.html
    INFO 7.06f conversion went smoothly.
    INFO Parsing 7.07d
    INFO HTML saved at /home/arthurazs/changelogs/707d.html
    WARNING 7.07d had 3 lines under GENERAL updates:
    * Added the following abilities to Ability Draft: Fire Remnant, Psionic Trap, Chakram
    * Neutral Ancients gold bounties reduced by 10%
    * Arcane Rune: Manacost Reduction reduced from 40% to 30% (same as the cooldown reduction)

    Some of these lines might be hero/item updates and you should manually
    place them at the proper location.

Make sure that ``<filename>`` is in your current directory. You can also
provide the ``path`` to the changelog.

::

    $ dotapatch /home/arthurazs/changelogs/706f
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/706f.html
    INFO 7.06f conversion went smoothly.

**P.S.** If the HTML page shows some of the heroes/items as
``[[hero_name]]`` instead of the hero/item's ``picture``, run the
following:

::

    $ dotapatch --update-data
    INFO Downloading itemdata from dota2's heropediadata
    INFO Updated itemdata saved successfully
    INFO Downloading herodata from dota2's heropediadata
    INFO Updated herodata saved successfully

This will require internet connection and may take a while but it will
ensure that the HeropediaData gets up-to-date.

Getting started
---------------

You will need python.

::

    $ sudo apt-get install python

How does it work
~~~~~~~~~~~~~~~~

::

    $ dotapatch -h
    usage: dotapatch [-h] [-t template_file] [-u] [-V] [-d] [-s] [-q]
                     [changelog_file [changelog_file ...]]

    Parses Dota 2 text patches to html format.

    positional arguments:
      changelog_file        changelog to be formated

    optional arguments:
      -h, --help            show this help message and exit
      -t template_file, --template template_file
                            base template to generate HTML
      -u, --update-data     force heropediadata update
      -V, --version         show program's version number and exit

    logging arguments:
      -d, --debug           set verbosity level to DEBUG
      -s, --save-log        save log output
      -q, --quiet           less verbose

Run **dotapatch** stating the full path to the file:

::

    $ dotapatch /home/arthurazs/changelogs/706f
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/706f.html
    INFO 7.06f conversion went smoothly.

Or you can head over to the directory with the changelog and run
**dotapatch** stating only the filename:

::

    $ cd changelogs
    $ dotapatch 706f
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/changelogs/706f.html
    INFO 7.06f conversion went smoothly.

It's possible to parse many changelogs at once, enter as many files as
you want:

::

    $ cd changelogs
    $ dotapatch 706f 707b 707d
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/changelogs/706f.html
    INFO 7.06f conversion went smoothly.
    INFO Parsing 7.07b
    INFO HTML saved at /home/arthurazs/git/dotapatch/707b.html
    WARNING 7.07b had 1 line under GENERAL updates:
    * Backdoor Protection damage reduction increased from 25% to 40%

    This line might be a hero/item update and you should manually place it
    at the proper location.
    INFO Parsing 7.07d
    INFO HTML saved at /home/arthurazs/changelogs/707d.html
    WARNING 7.07d had 3 lines under GENERAL updates:
    * Added the following abilities to Ability Draft: Fire Remnant, Psionic Trap, Chakram
    * Neutral Ancients gold bounties reduced by 10%
    * Arcane Rune: Manacost Reduction reduced from 40% to 30% (same as the cooldown reduction)

    Some of these lines might be hero/item updates and you should manually
    place them at the proper location.

There are some optional arguments that you can use:

::

    $ dotapatch --version
    dotapatch: v2.3.2

    $ dotapatch --update-data
    INFO Downloading itemdata from dota2's heropediadata
    INFO Updated itemdata saved successfully
    INFO Downloading herodata from dota2's heropediadata
    INFO Updated herodata saved successfully

    $ dotapatch 706f --update-data
    INFO Downloading itemdata from dota2's heropediadata
    INFO Updated itemdata saved successfully
    INFO Downloading herodata from dota2's heropediadata
    INFO Updated herodata saved successfully
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/changelogs/706f.html
    INFO 7.06f conversion went smoothly.

    $ dotapatch 706f --quiet

    $ dotapatch 706f --debug
    DEBUG Reading changelog.
    DEBUG Parsing changelog.
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/changelogs/706f.html
    INFO 7.06f conversion went smoothly.

    $ dotapatch dotapatch/changelogs/706f --save-log
    INFO Recording log file at /home/arthurazs/dotapatch.log
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/706f.html
    INFO 7.06f conversion went smoothly.

    $ dotapatch dotapatch/changelogs/706f --template gh-pages
    INFO 7.06f using 'gh-pages' template.
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/706f.html
    INFO 7.06f conversion went smoothly.

-  ``--template`` indicates which template is going to be used to parse
   the changelog. The ``default`` template generates a standalone HTML
   that uses `dota2 <http://dota2.com>`__ css files.
-  ``--debug`` and ``--quiet`` increase and decrease **dotapatch**'s
   verbosity, respectively.
-  ``--save-log`` saves a log with maximum verbosity output.
-  ``--update-data`` requires internet connection. It will ensure that
   the HeropediaData gets up-to-date.

Using dotapatch
---------------

Installing dotapatch
~~~~~~~~~~~~~~~~~~~~

Install **dotapatch** using ``pip``:

::

    $ pip install dotapatch
    $ dotapatch
    usage: dotapatch [-h] [-t template_file] [-u] [-V] [-d] [-s] [-q]
                     [changelog_file [changelog_file ...]]

Or `clone (or
download) <https://help.github.com/articles/cloning-a-repository>`__
this `repository <https://github.com/arthurazs/dotapatch>`__, head over
to the folder and install using the ``setup.py``:

::

    $ git clone https://github.com/arthurazs/dotapatch.git
    $ cd dotapatch
    $ python setup.py install
    $ dotapatch
    usage: dotapatch [-h] [-t template_file] [-u] [-V] [-d] [-s] [-q]
                     [changelog_file [changelog_file ...]]

**OPTIONALLY** You can use **dotapatch** without installing. Just `clone
(or download) <https://help.github.com/articles/cloning-a-repository>`__
the `repository <https://github.com/arthurazs/dotapatch>`__.

::

    $ git clone https://github.com/arthurazs/dotapatch.git
    $ cd dotapatch
    $ python -m dotapatch
    usage: dotapatch [-h] [-t template_file] [-u] [-V] [-d] [-s] [-q]
                     [changelog_file [changelog_file ...]]

Gathering a new changelog
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Go to `dota2 news <https://www.dota2.com/news/updates>`__ page and
   locate the latest **patch**.
-  Copy and save it as a file.

   -  The content you save **must** start with the patch name followed
      by colon (e.g. ``7.07d:``).
   -  The second line won't be read, so you can leave it with anything
      other than a real changelog line (e.g. ``--``).
   -  **All** the following lines **must** start with a star/asterisk
      (e.g. ``* Anti-mage magic resistance reduced by a lot``).

   ::

       7.07d:
       ==
       * Necronomicon: Mana Break damage from 60 to 50%
       * Nullifier: Cooldown reduced from 14 to 13
       * Nullifier: Manacost reduced from 100 to 75

       * Alchemist: Unstable Concoction damage increased from 150/220/290/360 to 160/240/320/400
       * Bane: Enfeeble duration reduced from 20 to 14/16/18/20
       * Bane: Brain Sap damage rescaled from 90/160/230/300 to 75/150/225/300

Running dotapatch
~~~~~~~~~~~~~~~~~

If you've installed **dotapatch**, head over to the folder where you
saved the changelog file and run **dotapatch**.

::

    $ cd changelogs
    $ dotapatch 706f
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/changelogs/706f.html
    INFO 7.06f conversion went smoothly.

If you haven't installed **dotapatch**, head over to the **dotapatch**
folder and run **dotapatch** as a **module**.

::

    $ cd dotapatch
    $ python -m dotapatch /home/arthurazs/changelogs/706f
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/dotapatch/706f.html
    INFO 7.06f conversion went smoothly.

Testing dotapatch
~~~~~~~~~~~~~~~~~

You can test either using `tox <#tox>`__ or `nosetests <#nosetests>`__.

It's recomended to use **tox** in order to test the code under several
Python versions at once. Tox will automatically skip versions that are
not installed, no worries!

tox
^^^

You will need ``tox``:

::

    $ pip install tox

`Clone (or
download) <https://help.github.com/articles/cloning-a-repository>`__
this `repository <https://github.com/arthurazs/dotapatch>`__, head over
to the folder and run ``tox``:

::

    $ git clone https://github.com/arthurazs/dotapatch.git
    $ cd dotapatch
    $ tox
    GLOB sdist-make: /home/arthurazs/git/dotapatch/setup.py
    py27 inst-nodeps: /home/arthurazs/git/dotapatch/.tox/dist/dotapatch-2.3.2.zip
    [...]
    26 tests run in 0.166 seconds (26 tests passed)
    py33 create: /home/arthurazs/git/dotapatch/.tox/py33
    ERROR: InterpreterNotFound: python3.3
    py34 create: /home/arthurazs/git/dotapatch/.tox/py34
    ERROR: InterpreterNotFound: python3.4
    py35 inst-nodeps: /home/arthurazs/git/dotapatch/.tox/dist/dotapatch-2.3.2.zip
    [...]
    26 tests run in 0.172 seconds (26 tests passed)
    py36 create: /home/arthurazs/git/dotapatch/.tox/py36
    ERROR: InterpreterNotFound: python3.6
    _________________________________ summary ___________________________________
      py27: commands succeeded
    SKIPPED:  py33: InterpreterNotFound: python3.3
    SKIPPED:  py34: InterpreterNotFound: python3.4
      py35: commands succeeded
    SKIPPED:  py36: InterpreterNotFound: python3.6
      congratulations :)

nosetests
^^^^^^^^^

You will need ``nosetests`` but the setup.py will handle it.

`Clone (or
download) <https://help.github.com/articles/cloning-a-repository>`__
this `repository <https://github.com/arthurazs/dotapatch>`__, head over
to the folder and run the test:

::

    $ python setup.py test
    running nosetests
    [...]
    file: assert 'itemdata' file exists ... passed
    str: sort_item("sphere") returns "linken s sphere" ... passed
    hero: get_hero_name(hero) returns hero_id ... passed
    item: get_hero_name(item) returns None ... passed
    main: assert get_parser() returns default values ... passed
    html: assert item content is added properly ... passed
    tmpl: raise error for malformed template ... passed
    ptc: parse file with GENERAL section and return 1 (or greater) ... passed
    [...]
    -------------------------------------------------------------------------
    26 tests run in 0.174 seconds (26 tests passed)

Built with
----------

**dotapatch** uses the following libraries:

-  `\_\_future\_\_ <https://docs.python.org/3/reference/simple_stmts.html#future-statements>`__
   Ensures backwards compatibility
-  `os <https://docs.python.org/3/library/os.html>`__ Portable way of
   using operating system dependent functionalities

   -  `os.path <https://docs.python.org/3/library/os.path.html>`__ Makes
      sure all directories are created and all data are downloaded
   -  `os.makedirs <https://docs.python.org/3/library/os.html#os.makedirs>`__
      Creates HeropediaData directory
   -  `os.remove <https://docs.python.org/3/library/os.html#os.remove>`__
      Clean data generated during the tests
   -  `os.rename <https://docs.python.org/3/library/os.html#os.rename>`__
      Persists original data after testing

-  `json.loads <https://docs.python.org/3/library/json.html#json.loads>`__
   Parses json from HeropediaData to a Python dictionary
-  `ast.literal\_eval <https://docs.python.org/3/library/ast.html#ast.literal_eval>`__
   Parses data from file to a Python dictionary
-  `argparse.ArgumentParser <https://docs.python.org/3/library/argparse.html#argumentparser-objects>`__
   Enables the use of arguments. Try ``$ dotapatch -h``
-  `collections.defaultdict <https://docs.python.org/3/library/collections.html#collections.defaultdict>`__

   -  defaultdict(list) stores each line of the changelog inside a list
      (inside a dictionary)
   -  Each ``dictionary.keys()`` (hero) stores ``dictionary.values()``
      (hero changes)
   -  ``dictionary.values()`` returns a list with all changes

-  `urllib.urlopen <https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen>`__
   Fetches HeropediaData files

   -  `urllib2.urlopen <https://docs.python.org/2/library/urllib2.html#urllib2.urlopen>`__
      for Python 2
   -  `urllib.request.urlopen <https://docs.python.org/3/library/urllib.request.html#urllib.request.urlopen>`__
      for Python 3

-  `logging <https://docs.python.org/3/library/logging.html>`__ Manages
   *dotapatch* logs

   -  `DEBUG <https://docs.python.org/3/library/logging.html#logging-levels>`__
      The numeric value of logging level for debugging
   -  `StreamHandler <https://docs.python.org/3/library/logging.handlers.html#streamhandler>`__
      Manages the logging output
   -  `Formatter <https://docs.python.org/3/library/logging.html#logging.Formatter>`__
      Formats the logging output
   -  `FileHandler <https://docs.python.org/3/library/logging.handlers.html#filehandler>`__
      Saves the logging output into a file
   -  `getLogger <https://docs.python.org/3/library/logging.html#logging.getLogger>`__
      Keeps logger consistent between classes
   -  `getLevelName <https://docs.python.org/3/library/logging.html#logging.getLevelName>`__
      Returns the numeric value of a string logging level

-  `tox <https://tox.readthedocs.io>`__ Run tests for Python (2.7, 3.3,
   3.4, 3.5, 3.6)

   -  `unittest <https://docs.python.org/3/library/unittest.html>`__
      Base for the tests

      -  `mock.patch <https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch>`__
         replaces system argv with mock args
      -  `nose <http://nose.readthedocs.io/en/latest>`__ test suite
         (nosetests)

         -  `rednose <https://github.com/JBKahn/rednose>`__ plugging
            which improves readability
         -  `coverage <http://coverage.readthedocs.io/en/coverage-4.4.2/>`__
            tool for measuring code coverage

-  `pip <https://pypi.python.org/pypi>`__ Installation manager

   -  `setuptools <https://github.com/pypa/setuptools>`__ Setup manager

Authors
-------

-  `Arthur Zopellaro <https://github.com/arthurazs>`__

   -  Maintainer

Task list
---------

-  **TODO** see
   `projects <https://github.com/arthurazs/dotapatch/projects>`__.
-  **Changelog** see
   `releases <https://github.com/arthurazs/dotapatch/releases>`__.

Contributing
------------

Do you have any feedback, questions or ideias? Do you want to report a
bug? Even better, would you like to fix a bug or implement a feature?

First of all, thank you! Please, read the `Contributing
Guidelines <https://github.com/arthurazs/dotapatch/blob/master/CONTRIBUTING.md>`__
for details.

-  Open an `issue <https://github.com/arthurazs/dotapatch/issues/new>`__
   if you have any feedback, questions, ideias or to report a bug.
-  Open a `pull
   request <https://github.com/arthurazs/dotapatch/compare>`__ after you
   implement a feature or fix a bug.

Code of Conduct
---------------

The `Code of
Conduct <https://github.com/arthurazs/dotapatch/blob/master/CODE_OF_CONDUCT.md>`__
for this project is based on `Contributor
Covenant <https://www.contributor-covenant.org>`__.

Any unacceptable behavior may be reported by contacting the project team
at arthurazsoares@gmail.com.

License
-------

This project is licensed under the `MIT
License <https://github.com/arthurazs/dotapatch/blob/master/LICENSE>`__.

.. |GitHub Release| image:: https://img.shields.io/github/release/arthurazs/dotapatch.svg
   :target: https://github.com/arthurazs/dotapatch/releases
.. |GitHub Tag| image:: https://img.shields.io/github/tag/arthurazs/dotapatch.svg
   :target: https://github.com/arthurazs/dotapatch/tags
.. |GitHub License| image:: https://img.shields.io/github/license/arthurazs/dotapatch.svg
   :target: https://github.com/arthurazs/dotapatch/blob/master/LICENSE
.. |GitHub Issues| image:: https://img.shields.io/github/issues/arthurazs/dotapatch.svg
   :target: https://github.com/arthurazs/dotapatch/issues
.. |GitHub Pull Requests| image:: https://img.shields.io/github/issues-pr/arthurazs/dotapatch.svg
   :target: https://github.com/arthurazs/dotapatch/pulls
.. |PyPI Version| image:: https://img.shields.io/pypi/v/dotapatch.svg
   :target: https://pypi.python.org/pypi/dotapatch
.. |PyPI License| image:: https://img.shields.io/pypi/l/dotapatch.svg
   :target: https://pypi.python.org/pypi/dotapatch
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/dotapatch.svg
   :target: https://pypi.python.org/pypi/dotapatch#downloads
.. |PyPI Wheel| image:: https://img.shields.io/pypi/wheel/dotapatch.svg
   :target: https://pypi.python.org/pypi/dotapatch#downloads
.. |PyPI Status| image:: https://img.shields.io/pypi/status/dotapatch.svg
   :target: https://pypi.python.org/pypi/dotapatch
.. |CircleCI| image:: https://img.shields.io/circleci/project/github/arthurazs/dotapatch.svg
   :target: https://circleci.com/gh/arthurazs/dotapatch
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Grade/f92dab093ac0404fa76deb1b1ce23ea2
   :target: https://www.codacy.com/app/arthurazsoares/dota2patches?utm_source=github.com&utm_medium=referral&utm_content=arthurazs/dota2patches&utm_campaign=Badge_Grade
.. |Codacy Badge| image:: https://api.codacy.com/project/badge/Coverage/f92dab093ac0404fa76deb1b1ce23ea2
   :target: https://www.codacy.com/app/arthurazsoares/dota2patches?utm_source=github.com&utm_medium=referral&utm_content=arthurazs/dota2patches&utm_campaign=Badge_Coverage
.. |codecov| image:: https://codecov.io/gh/arthurazs/dotapatch/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/arthurazs/dotapatch
