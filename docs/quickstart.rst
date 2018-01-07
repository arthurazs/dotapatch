.. highlight:: console

Quickstart
==========

.. contents:: :depth: 3

Installing dotapatch
--------------------

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
-------------------------

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
-----------------

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
