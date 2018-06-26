About dotapatch
===============

======== ======
Platform Status
======== ======
GitHub   |Release| |Tag| |License| |Issues| |PR|
PyPI     |PVersion| |PLicense| |Version| |Wheel| |Status|
Health   |CI| |docs| |CIssues| |Coverage| |codecov|
======== ======

.. |Release|    image:: https://img.shields.io/github/release/arthurazs/
                        dotapatch.svg
               :target: https://github.com/arthurazs/dotapatch/releases
.. |Tag|        image:: https://img.shields.io/github/tag/arthurazs/
                        dotapatch.svg
               :target: https://github.com/arthurazs/dotapatch/tags
.. |License|    image:: https://img.shields.io/github/license/arthurazs/
                        dotapatch.svg
               :target: https://github.com/arthurazs/dotapatch/blob/master/
                        LICENSE
.. |Issues|     image:: https://img.shields.io/github/issues/arthurazs/
                        dotapatch.svg
               :target: https://github.com/arthurazs/dotapatch/issues
.. |PR|         image:: https://img.shields.io/github/issues-pr/arthurazs/
                        dotapatch.svg
               :target: https://github.com/arthurazs/dotapatch/pulls
.. |PVersion|   image:: https://img.shields.io/pypi/v/dotapatch.svg
               :target: https://pypi.python.org/pypi/dotapatch
.. |PLicense|   image:: https://img.shields.io/pypi/l/dotapatch.svg
               :target: https://pypi.python.org/pypi/dotapatch
.. |Version|    image:: https://img.shields.io/pypi/pyversions/dotapatch.svg
               :target: https://pypi.python.org/pypi/dotapatch#downloads
.. |Wheel|      image:: https://img.shields.io/pypi/wheel/dotapatch.svg
               :target: https://pypi.python.org/pypi/dotapatch#downloads
.. |Status|     image:: https://img.shields.io/pypi/status/dotapatch.svg
               :target: https://pypi.python.org/pypi/dotapatch
.. |CI|         image:: https://img.shields.io/circleci/project/github/
                        arthurazs/dotapatch.svg
               :target: https://circleci.com/gh/arthurazs/dotapatch
.. |docs|       image:: https://readthedocs.org/projects/dotapatch/badge/
                        ?version=latest
               :target: https://dotapatch.readthedocs.io/en/latest/
                        ?badge=latest
.. |CIssues|    image:: https://api.codacy.com/project/badge/Grade/
                        f92dab093ac0404fa76deb1b1ce23ea2
               :target: https://www.codacy.com/app/arthurazsoares/dota2patches?
                        utm_source=github.com&utm_medium=referral&utm_content=
                        arthurazs/dota2patches&utm_campaign=Badge_Grade
.. |Coverage|   image:: https://api.codacy.com/project/badge/Coverage/
                        f92dab093ac0404fa76deb1b1ce23ea2
               :target: https://www.codacy.com/app/arthurazsoares/dota2patches?
                        utm_source=github.com&utm_medium=referral&utm_content=
                        arthurazs/dota2patches&utm_campaign=Badge_Coverage
.. |codecov|    image:: https://codecov.io/gh/arthurazs/dotapatch/branch/master
                        /graph/badge.svg
               :target: https://codecov.io/gh/arthurazs/dotapatch

**dotapatch** is a software which aims the automation of formatting
``simple text changelog`` into ``clear html changelog``.

Check the `Gameplay Update 7.18`_. This is the latest patch parsed using
**dotapatch**.

.. _Gameplay Update 7.18: https://arthurazs.github.io/dotapatch/718.html

Read the documentation at `Read the Docs`_.

.. _Read the Docs: https://dotapatch.readthedocs.io/

.. contents:: :depth: 2

Quickstart
----------

Installing dotapatch
~~~~~~~~~~~~~~~~~~~~

Install **dotapatch** using pip_:

.. _pip: https://pip.pypa.io/en/stable/installing/

::

    $ pip install dotapatch
    Collecting dotapatch
    ...
    Successfully installed dotapatch-2.4
    $ dotapatch
    usage: dotapatch [-h] [-t template_file] [-u] [-V] [-d] [-s] [-q]
                     [changelog_file [changelog_file ...]]

.. note::
    If you get an ``OSError``, run ``pip install --user dotapatch`` instead.


Gathering a new changelog
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to `dota2 news`_ page and locate the latest **patch**.
2. Copy and save it as a file.

.. _dota2 news:     https://www.dota2.com/news/updates

::

    7.07d:
    ==
    * Necronomicon: Mana Break damage from 60 to 50%
    * Nullifier: Cooldown reduced from 14 to 13
    * Nullifier: Manacost reduced from 100 to 75

    * Alchemist: Unstable Concoction damage increased from 150/220/290/360 to 160/240/320/400
    * Bane: Enfeeble duration reduced from 20 to 14/16/18/20
    * Bane: Brain Sap damage rescaled from 90/160/230/300 to 75/150/225/300

.. warning::

    The content **must** start with the patch name ``7.07d:`` followed by a
    separator ``==``.

Running dotapatch
~~~~~~~~~~~~~~~~~

Head over to the folder where you saved the changelog file and run
**dotapatch**:

::

    $ cd changelogs
    $ dotapatch 706f
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/changelogs/706f.html
    INFO 7.06f conversion went smoothly.

.. note::

    If the HTML page shows some of the heroes/items as ``[[hero_name]]`` instead
    of the hero/item's ``picture``, run the following:

    ::

        $ dotapatch --update-data
        INFO Downloading itemdata from dota2's heropediadata
        INFO Updated itemdata saved successfully
        INFO Downloading herodata from dota2's heropediadata
        INFO Updated herodata saved successfully

    This will require internet connection and may take a while but it will
    ensure that the HeropediaData gets up-to-date.

Task List
---------

-  **TODO** see projects_.
-  **Changelog** see releases_.

.. _projects:   https://github.com/arthurazs/dotapatch/projects
.. _releases:   https://github.com/arthurazs/dotapatch/releases

Contributing
------------

Take a time to read our `Code of Conduct`_. Any unacceptable behavior shall be
reported by contacting the project team at arthurazsoares@gmail.com.

- Do you have any feedback, questions or ideias?
- Do you want to report a bug?
- Would you like to fix a bug or implement a feature?

First of all, thank you! Please, read our `Contributing Guidelines`_ for
details.

This project is licensed under the `MIT License`_.

.. _Contributing Guidelines:    https://github.com/arthurazs/dotapatch/blob/
                                master/CONTRIBUTING.rst
.. _Code of Conduct:            https://github.com/arthurazs/dotapatch/blob/
                                master/CODE_OF_CONDUCT.rst
.. _MIT License:                https://github.com/arthurazs/dotapatch/blob/
                                master/LICENSE
