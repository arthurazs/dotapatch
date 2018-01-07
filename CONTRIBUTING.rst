Contributing Guidelines
=======================

Please, don't forget to read our `Code of Conduct`_ to make sure you don't
violate any of the rules.

.. _Code of Conduct:  https://github.com/arthurazs/dotapatch/blob/master/
                      CODE_OF_CONDUCT.rst

.. contents::

Issues
------

Please open a `new issue`_ if you have any feedback, questions, ideias or to
report a bug.

.. _new issue:  https://github.com/arthurazs/dotapatch/issues/new

Pull Requests
-------------

First you should fork_ the repository and make sure the tests are passing:

.. _fork: https://help.github.com/articles/fork-a-repo

::

    $ python setup.py test
    -----------------------------------------------
    23 tests run in 0.208 seconds (23 tests passed)

Then, create a test_ for the fix/feature you intend to code and run the test
again:

.. _test: https://docs.python.org/3/library/unittest.html

::

    $ python setup.py test
    tests the found bug ... FAILED
    ======================================================
    1) FAIL: tests the found bug
    ------------------------------------------------------
       Traceback (most recent call last):
        tests/test_patch.py line 15 in test_bug_found
          self.fail()
       AssertionError: None
           """Fail immediately, with the given message."""
       >>  raise self.failureException(None)
    ------------------------------------------------------
    24 tests run in 0.205 seconds.
    1 FAILED (23 tests passed)

Finally, fix the bug/implement the feature. Make sure the test passes
now:

::

    $ python setup.py test
    -----------------------------------------------
    24 tests run in 0.208 seconds (24 tests passed)

Open a `pull request`_ explaining your code. Feel free to add your name as a
contributor in the Authors_ file.

.. _pull request: https://github.com/arthurazs/dotapatch/compare
.. _Authors:      https://github.com/arthurazs/dotapatch/blob/master/
                  AUTHORS.rst
