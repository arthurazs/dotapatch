Dota 2: Changelog formatted as it should.
=========================================

+------------+-----------------------------------------------------------------------------------------+
| Platform   | Status                                                                                  |
+============+=========================================================================================+
| GitHub     | |GitHub Release| |GitHub Tag| |GitHub License| |GitHub Issues| |GitHub Pull Requests|   |
+------------+-----------------------------------------------------------------------------------------+
| PyPI       | |PyPI Version| |PyPI License| |Python Version| |PyPI Wheel| |PyPI Status|               |
+------------+-----------------------------------------------------------------------------------------+
| CircleCI   | |CircleCI|                                                                              |
+------------+-----------------------------------------------------------------------------------------+

**dotapatch** is a software which aims the automation of formatting
``simple text changelog`` into ``clear html changelog``.

Check the `Gameplay Update
6.88f <https://arthurazs.github.io/dotapatch/688f.html>`__. This is the
latest patch parsed using **dotapatch**.

**Contents**

-  `Too long; didn't read <#tl-dr>`__
-  `Getting started <#getting-started>`__

   -  `How does it work <#how-does-it-work>`__

-  `Using dotapatch <#using-dotapatch>`__

   -  `Installing dotapatch <#installing-dotapatch>`__
   -  `Gathering a new changelog <#gathering-a-new-changelog>`__
   -  `Running dotapatch <#running-dotapatch>`__
   -  `Testing dotapatch <#testing-dotapatch>`__

-  `Built with <#built-with>`__
-  `Authors <#authors>`__
-  `Task list <#task-list>`__
-  `Contributing <#contributing>`__
-  `License <#license>`__

TL;DR
-----

::

    $ pip install dotapatch

Save a changelog file in accordance with the following format:

::

    6.88f:
    --
    * Purifying Flames manacost increased from 50/60/70/80 to 80/85/90/95
    * Morphling base damage reduced by 4
    * Nyx's Scepter Burrow cast time increased from 1 to 1.5
    * Fixed Return working on Centaur Illusions

Head over to the directory you saved the changelog and run
**dotapatch**.

::

    $ cd Desktop/changelogs
    $ dotapatch 688f
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/688f.html
    INFO Conversion went smoothly.

Make sure that ``<filename>`` is in your current directory. You can also
provide the ``path`` to the changelog.

::

    $ dotapatch /home/arthurazs/Desktop/changelogs/688f
    INFO HTML saved at /home/arthurazs/688f.html
    INFO Conversion went smoothly.

Getting started
---------------

You will need python.

::

    $ sudo apt-get install python

How does it work
~~~~~~~~~~~~~~~~

::

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

::

    $ dotapatch /home/arthurazs/Desktop/changelogs/688f
    INFO HTML saved at /home/arthurazs/688f.html
    INFO Conversion went smoothly.

Or you can head over to the directory with the changelog and run
**dotapatch** stating only the filename:

::

    $ cd Desktop/changelogs
    $ dotapatch 688f
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/688f.html
    INFO Conversion went smoothly.

There are some optional arguments that you can use:

::

    $ dotapatch --version
    dotapatch: v2.0

    $ dotapatch 688f
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/688f.html
    INFO Conversion went smoothly.

    $ dotapatch 688f --quiet

    $ dotapatch 688f --debug
    DEBUG Reading changelog.
    DEBUG Parsing changelog.
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/688f.html
    INFO Conversion went smoothly.

    $ dotapatch dotapatch/changelogs/688f --save-log
    INFO Recording log file at /home/arthurazs/git/dotapatch/dotapatch.log
    INFO HTML saved at /home/arthurazs/git/dotapatch/688f.html
    INFO Conversion went smoothly.

    $ dotapatch dotapatch/changelogs/688f --template gh-pages
    INFO Using 'gh-pages' template.
    INFO HTML saved at /home/arthurazs/git/dotapatch/688f.html
    INFO Conversion went smoothly.

-  ``--template`` indicates which template is going to be used to parse
   the changelog. The ``default`` template generates a standalone HTML
   that uses `dota2 <http://dota2.com>`__ css files.
-  ``--debug`` and ``--quiet`` increase and decrease **dotapatch**'s
   verbosity, respectively.
-  ``--save-log`` saves a log with maximum verbosity output.

Using dotapatch
---------------

Installing dotapatch
~~~~~~~~~~~~~~~~~~~~~~~~~~

Install **dotapatch** using ``pip``:

::

    $ pip install dotapatch

You might get ``PermissionError``. Refer to the
`FAQ <https://github.com/arthurazs/dotapatch/blob/master/FAQ.md>`__ on how to fix this issue.

Or `clone (or
download) <https://help.github.com/articles/cloning-a-repository/>`__
this `repository <https://github.com/arthurazs/dotapatch>`__, head over to the folder and install using
the ``setup.py``:

::

    $ git clone https://github.com/arthurazs/dotapatch.git
    $ cd dotapatch
    $ python setup.py install

You might get the same ``PermissionError``. Refer to the
`FAQ <https://github.com/arthurazs/dotapatch/blob/master/FAQ.md>`__ on how to fix this issue.

**OPTIONALLY** You can use **dotapatch** without installing. Just `clone
(or
download) <https://help.github.com/articles/cloning-a-repository/>`__
the `repository <https://github.com/arthurazs/dotapatch>`__.

::

    $ git clone https://github.com/arthurazs/dotapatch.git

Gathering a new changelog
~~~~~~~~~~~~~~~~~~~~~~~~~

-  Go to `dota2 news <https://www.dota2.com/news/updates/>`__ page and
   locate the latest **patch**.
-  Copy and save it as a file.

   -  The content you save **must** start with the patch name followed
      by colon (e.g. ``6.88f:``).
   -  The second line won't be read, so you can leave it with anything
      other than a real changelog line (e.g. ``--``).
   -  **All** the following lines **must** start with a star/asterisk
      (e.g. ``* Anti-mage magic resistance reduced by a lot``).

   ::

       6.88f:
       --
       * Purifying Flames manacost increased from 50/60/70/80 to 80/85/90/95
       * Torrent cooldown increased from 10 to 16/14/12/10
       * Ghostship Rum damage reduction changed from 50% to 40/45/50%
       * Shadow Poison manacost increased from 40 to 55
       * Atrophy Aura attack damage reduction changed from 18/26/34/42% to 10/20/30/40%
       * Morph Replicate cast time increased from 0.25 to 0.35
       * Morphling base damage reduced by 4
       * Drow Ranger strength gain reduced from 1.9 to 1.6
       * Purification cast range reduced from 700 to 575
       * Purification cast point reduced from 0.25 to 0.2
       * Purification cooldown reduced from 10 to 9
       * Repel duration rescaled from 4/6/8/10 to 5/6/7/8
       * Repel cooldown reduced from 14 to 20/18/16/14
       * Outworld Devourer base damage reduced by 6
       * Starfall Scepter cooldown increased from 9 to 10
       * Faceless Void base armor reduced by 1
       * Stifling Dagger cast range reduced from 825/950/1075/1200 to 525/750/975/1200 
       * Spark Wraith no longer dispels (still slows)
       * Arc Warden movement speed reduced by 10
       * Healing Ward manacost increased from 120/125/130/135 to 140
       * Smoke Screen slow reduced from 19/21/23/25% to 13/17/21/25%
       * Track movement speed bonus reduced from 20% to 16/18/20%
       * Nyx's Scepter Burrow cast time increased from 1 to 1.5
       * Flamebreak knockback no longer interrupts channeling spells (behaves like blinding light)
       * Flamebreak burn duration increased from 3/4/5/6 to 4/5/6/7 (total damage increased)
       * Fixed Return working on Centaur Illusions

Running dotapatch
~~~~~~~~~~~~~~~~~

If you've installed **dotapatch**, head over to the folder where you
saved the changelog file and run **dotapatch**.

::

    $ cd Desktop/changelogs
    $ dotapatch 688f
    INFO HTML saved at /home/arthurazs/Desktop/changelogs/688f.html
    INFO Conversion went smoothly.

If you haven't installed **dotapatch**, head over to the **dotapatch**
folder and run **dotapatch** as a **module**.

::

    $ cd Desktop/dotapatch
    $ python -m dotapatch /home/arthurazs/Desktop/changelogs/688f
    INFO HTML saved at /home/arthurazs/Desktop/dotapatch/688f.html
    INFO Conversion went smoothly.

Testing dotapatch
~~~~~~~~~~~~~~~~~

You will need ``tox``:

::

    $ pip install tox

`Clone (or
download) <https://help.github.com/articles/cloning-a-repository/>`__
this `repository <https://github.com/arthurazs/dotapatch>`__, head over to the folder and run ``tox``:

::

    $ git clone https://github.com/arthurazs/dotapatch.git
    $ cd dotapatch
    $ tox

Built with
----------

**dotapatch** uses the following libraries:

-  `ast <https://docs.python.org/3.4/library/ast.html>`__

   -  Transforms data from HeropediaData into dictionary

-  `os.path <https://docs.python.org/3.4/library/os.path.html>`__

   -  Makes sure all directories are created and all data are downloaded

-  `argparse <https://docs.python.org/3.4/library/argparse.html>`__

   -  Enables the use of arguments. Try ``$ ./patch.py -h``

-  collections.\ `defaultdict <https://docs.python.org/3.4/library/collections.html#collections.defaultdict>`__

   -  defaultdict(list) stores each line of the changelog inside a list
      (inside a dictionary)
   -  Each ``dictionary.keys()`` (hero) stores ``dictionary.values()``
      (hero changes)
   -  ``dictionary.values()`` returns a list with all changes

-  `requests <https://github.com/kennethreitz/requests>`__

   -  Fetches HeropediaData files

-  `logging <https://docs.python.org/3.4/library/logging.html>`__

   -  Manage *dotapatch* logs

-  `tox <https://tox.readthedocs.io>`__

   -  Run tests for Python 2.7 and Python 3.4

      -  `unittest <https://docs.python.org/3.4/library/unittest.html>`__

         -  Base for the tests
         -  `nose <http://nose.readthedocs.io/en/latest/>`__ test suite
            (nosetests)

            -  `--rednose <https://github.com/JBKahn/rednose>`__
               plugging which improves readability

-  `pip <https://pypi.python.org/pypi>`__

   -  Installation manager
   -  `setuptools <https://github.com/pypa/setuptools>`__

      -  Setup manager

Authors
-------

-  `**Arthur Zopellaro** <https://github.com/arthurazs>`__

   -  *Creator*

Task list
---------

-  **TODO** see `projects <https://github.com/arthurazs/dotapatch/projects>`__.
-  **Changelog** see `releases <https://github.com/arthurazs/dotapatch/releases>`__.

Contributing
------------

I need your help improving **dotapatch**! Please open `new
issues <https://github.com/arthurazs/dotapatch/issues/new>`__ if you have any feedback, questions or
ideias. Also, feel free to open `pull requests <https://github.com/arthurazs/dotapatch/compare>`__ if
you want to help me improve some of the code.

License
-------

This project is licensed under the `MIT License <https://github.com/arthurazs/dotapatch/blob/master/LICENSE>`__.

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
   :target: https://pypi.python.org/pypi/dotapatch
.. |PyPI Wheel| image:: https://img.shields.io/pypi/wheel/dotapatch.svg
   :target: https://pypi.python.org/pypi/dotapatch
.. |PyPI Status| image:: https://img.shields.io/pypi/status/dotapatch.svg
   :target: https://pypi.python.org/pypi/dotapatch
.. |CircleCI| image:: https://img.shields.io/circleci/project/github/arthurazs/dotapatch.svg
   :target: https://circleci.com/gh/arthurazs/dotapatch
