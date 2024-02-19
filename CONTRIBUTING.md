# Contributing Guidelines

**Style**: We conform to PEP-8 (in vscode use autopep8 extension),
and where that is silent we follow the
[Google style guide](https://google.github.io/styleguide/pyguide.html).

**Types**: We use type hints. Check with mypy
`$ mypy blah.py --ignore-missing-imports --ignore-used-before`.

**Testing**: We use the unittest framework. To run tests invoke
`$ python -m unittest -v`.

**Dependency Management**: We use poetry. Some common gestures:

```bash
$ poetry shell    # activate the virtual environment
$ code .          # open vscode within this venv
$ poetry add X --group dev # add a dev dependency X
$ poetry install  # install the dependencies in pyproject.toml or poetry.lock
```
