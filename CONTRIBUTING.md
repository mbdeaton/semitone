# Contributing Guidelines

**Style**: We conform to PEP-8 (in vscode use autopep8 extension),
and where that is silent we follow the
[Google style guide](https://google.github.io/styleguide/pyguide.html).
To automate this commitment, run black and pylint, which is configured to the
google pylintrc (with a few minor adjustments).
```bash
$ black .  # auto-format
$ pylint . # get style warnings
```

**Types**: We use type hints. Check with mypy

```bash
$ mypy blah.py --ignore-missing-imports --ignore-used-before
```

**Testing**: We use the unittest framework, tests are all feature tests,
written to validate some user need. Test logic should reflect how a user would
interact with this package. Test names follow the pattern `test_<verb phrase>`
to represent the corresponding user story of "I can <verb phrase>". To run
tests invoke

```bash
$ python -m unittest -v          # play all tests
$ python -m unittest -v testname # play one test
```

**Dependency Management**: We use poetry. Some common gestures:

```bash
$ poetry shell    # activate the virtual environment
$ code .          # open vscode within this venv
$ poetry add X --group dev # add a dev dependency X
$ poetry install  # install the dependencies in pyproject.toml or poetry.lock
```
