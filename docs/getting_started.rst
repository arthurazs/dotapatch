.. highlight:: console

Getting started
---------------

.. contents:: :depth: 3

Requirements
~~~~~~~~~~~~

You will need python.

.. image:: https://img.shields.io/pypi/pyversions/dotapatch.svg
    :target: https://pypi.python.org/pypi/dotapatch#downloads

::

    $ sudo apt-get install python

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

Or `clone/download`_ the repository_, head over to the folder and install it
using the ``setup.py``:

.. _clone/download: https://help.github.com/articles/cloning-a-repository
.. _repository: https://github.com/arthurazs/dotapatch

::

    $ git clone https://github.com/arthurazs/dotapatch.git
    Cloning into 'dotapatch'...
    ...
    Checking connectivity... done.
    $ cd dotapatch
    $ python setup.py install
    $ dotapatch
    usage: dotapatch [-h] [-t template_file] [-u] [-V] [-d] [-s] [-q]
                     [changelog_file [changelog_file ...]]

.. note::

    You can also use **dotapatch** without installing it:

    ::

        $ git clone https://github.com/arthurazs/dotapatch.git
        Cloning into 'dotapatch'...
        ...
        Checking connectivity... done.
        $ cd dotapatch
        $ python -m dotapatch
        usage: dotapatch [-h] [-t template_file] [-u] [-V] [-d] [-s] [-q]
                         [changelog_file [changelog_file ...]]

Gathering a new changelog
~~~~~~~~~~~~~~~~~~~~~~~~~

1. Go to `dota2 news`_ page and locate the latest **patch**.
2. Copy and save it as a file.

.. _dota2 news:     https://www.dota2.com/news/updates

.. code-block:: none

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

.. note::

    If you haven't installed **dotapatch**, head over to the **dotapatch**
    folder and run it as a **module**:

    ::

        $ cd dotapatch
        $ python -m dotapatch /home/arthurazs/changelogs/706f
        INFO Parsing 7.06f
        INFO HTML saved at /home/arthurazs/dotapatch/706f.html
        INFO 7.06f conversion went smoothly.

You may also run **dotapatch** stating the full path to the changelog file:

::

    $ dotapatch /home/arthurazs/changelogs/706f
    INFO Parsing 7.06f
    INFO HTML saved at /home/arthurazs/706f.html
    INFO 7.06f conversion went smoothly.

.. note::

    It's possible to parse many changelogs at once:

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
        * Arcane Rune: Manacost Reduction reduced from 40% to 30%

        Some of these lines might be hero/item updates and you should manually
        place them at the proper location.

Optional Arguments
++++++++++++++++++

There are some optional arguments that you can use:

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

.. note::

    - ``--update-data`` requires internet connection. It will ensure that the
      HeropediaData gets up-to-date.
    - ``--template`` indicates which template is going to be used to parse
      the changelog. The **default** template generates a standalone HTML
      that uses `dota2 <http://dota2.com>`__ css files.
    - ``--debug`` and ``--quiet`` respectively increase and decrease
      **dotapatch**'s verbosity.
    - ``--save-log`` saves a log with maximum verbosity output.
