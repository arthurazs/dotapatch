.. highlight:: console

Testing dotapatch
=================

|codacy| |codecov|

.. |codacy|     image:: https://api.codacy.com/project/badge/Coverage/
                        f92dab093ac0404fa76deb1b1ce23ea2
               :target: https://www.codacy.com/app/arthurazsoares/dota2patches?
                        utm_source=github.com&utm_medium=referral&utm_content=
                        arthurazs/dota2patches&utm_campaign=Badge_Coverage
.. |codecov|    image:: https://codecov.io/gh/arthurazs/dotapatch/branch/master/graph/
                        badge.svg
               :target: https://codecov.io/gh/arthurazs/dotapatch


You can test either using tox_ or nosetests_.

It's recomended to use ``tox`` in order to test the code under several Python
versions at once. ``Tox`` will automatically skip versions that are not
installed, so don't worry!

tox
---

You will need ``tox``:

::

    $ pip install tox

`Clone/download`_ the repository_, head over to the folder and run ``tox``:

.. _Clone/download: https://help.github.com/articles/cloning-a-repository
.. _repository: https://github.com/arthurazs/dotapatch

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
---------

You will need ``nosetests`` but the ``setup.py`` will handle it.

`Clone/download`_ the repository_, head over to the folder and run the test:

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
