# Contributing Guidelines

**Style**: We conform to PEP-8 and where that is silent we follow the
[Google style guide](https://google.github.io/styleguide/pyguide.html).
We also use type hints. To automate conformance run black, pylint, and mypy.
Pylint is configured to the google pylintrc (with a few minor adjustments).

```bash
$ black --line-length 80 .        # format to style
$ pylint .                        # get linting warnings
$ mypy --ignore-missing-imports . # get type-hinting warnings
```

**Testing**: We use the unittest framework. Tests are all feature tests,
written to validate some user need. Test logic should reflect how a user would
interact with this package. Test names follow the pattern `test_<verb phrase>`
to represent the corresponding user story of "I can [verb phrase]". To run
tests invoke

```bash
$ python -m unittest -v          # play all tests
$ python -m unittest -v testname # play one test
```

**Continuous Integration**: We use GitHub Actions to automatically run tests
and style checks/linting on every push and pull request to the `main` branch.

**Dependency Management**: We use poetry. Some common gestures:

```bash
$ poetry shell    # activate the virtual environment
$ code .          # open vscode within this venv
$ poetry add X --group dev # add a dev dependency X
$ poetry add X --optional # add optional dependency to main group note, you
                  # also need to manually add it to a named group under
                  # tool.poetry.extras
$ poetry install  # install the dependencies in pyproject.toml or poetry.lock
$ poetry install -E notebooks # install the extra dependencies for use of
                  # interactive notebooks
```

**Backlog**: A list of pending tasks lives in FUTURE.md.
