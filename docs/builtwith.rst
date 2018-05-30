Built with
----------

- `__future__`_ Ensures backwards compatibility
- :py:mod:`os` Portable way of using operating system dependent functionalities
    - :py:mod:`os.path` Makes sure all directories are created and all data are
      downloaded
    - :py:func:`os.makedirs` Creates HeropediaData directory
    - :py:func:`os.remove` Clean data generated during the tests
    - :py:func:`os.rename` Persists original data after testing
- :py:func:`json.loads` Parses json from HeropediaData to a Python dictionary
- :py:func:`ast.literal_eval` Parses data from file to a Python dictionary
- :py:class:`argparse.ArgumentParser` Enables the use of arguments. Try
  ``$ dotapatch -h``
- :py:class:`collections.defaultdict`
    - ``defaultdict(list)`` stores each line of the changelog inside a list
      (inside a dictionary)
    - Each ``dictionary.keys()`` (hero/item) stores ``dictionary.values()``
      (hero/item changes)
- ``urllib.urlopen`` Fetches HeropediaData files
    - urllib2.urlopen_ for Python 2
    - :py:func:`urllib.request.urlopen` for Python 3
- :py:mod:`logging` Manages *dotapatch* logs
    - DEBUG_ The numeric value of logging level for debugging
    - :py:class:`logging.StreamHandler` Manages the logging output
    - :py:class:`logging.Formatter` Formats the logging output
    - :py:class:`logging.FileHandler` Saves the logging output into a file
    - :py:func:`logging.getLogger` Keeps logger consistent between classes
    - :py:func:`logging.getLevelName` Returns the numeric value of a string
      logging level
- tox_ Run tests for Python (2.7, 3.4, 3.5, 3.6)
    - :py:mod:`unittest` Base for the tests
        - :py:func:`unittest.mock.patch` replaces system argv with mock args
        - nose_ test suite (nosetests)
            - rednose_ plugging which improves readability
            - coverage_ tool for measuring code coverage
- pip_ Installation manager
    - setuptools_ Setup manager


.. _\_\_future\_\_:     https://docs.python.org/3/reference/simple_stmts.html#
                        future-statements
.. _urllib2.urlopen:    https://docs.python.org/2/library/urllib2.html#
                        urllib2.urlopen
.. _DEBUG:              https://docs.python.org/3/library/logging.html#
                        logging-levels
.. _tox:                https://tox.readthedocs.io
.. _nose:               https://nose.readthedocs.io/en/latest
.. _rednose:            https://github.com/JBKahn/rednose
.. _coverage:           https://coverage.readthedocs.io/en/coverage-4.4.2/
.. _pip:                https://pypi.python.org/pypi
.. _setuptools:         https://github.com/pypa/setuptools
