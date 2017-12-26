# Contributing Guidelines

Please, don't forget to read our [Code of Conduct] to make sure you don't
violate any of the rules.

**Contents**

- [Issues](#issues)
- [Pull Requests](#pull-requests)

## Issues

Please open a [new issue] if you have any feedback, questions, ideias or to
report a bug.

## Pull Requests

First you should [fork] the repository and make sure the tests are passing:

    $ python setup.py test
    -----------------------------------------------
    23 tests run in 0.208 seconds (23 tests passed)

Then, create a [test] for the fix/feature you intend to code and run the
test again:

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

Finally, fix the bug/implement the feature. Make sure the test passes now:

    $ python setup.py test
    -----------------------------------------------
    24 tests run in 0.208 seconds (24 tests passed)

Open a [pull request] explaining your code. Feel free to add your name as a
contributor under **Authors** in the [README] file.

[new issue]:        https://github.com/arthurazs/dotapatch/issues/new
[pull request]:     https://github.com/arthurazs/dotapatch/compare
[fork]:             https://help.github.com/articles/fork-a-repo
[test]:             https://docs.python.org/3/library/unittest.html
[README]:           https://github.com/arthurazs/dotapatch/blob/master/README.md#authors
[Code of Conduct]:  https://github.com/arthurazs/dotapatch/blob/master/CODE_OF_CONDUCT.md
