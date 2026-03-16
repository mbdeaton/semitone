# Contributing Guidelines

## Quick start for contributors

1. **Clone the repository.**

   ```bash
   git clone https://github.com/mbdeaton/semitone.git
   cd semitone
   ```

2. **Install dependencies.**
   We use Poetry for dependency management.

   ```bash
   poetry install
   ```

3. **Activate the development environment.**

   ```bash
   eval $(poetry env activate)
   ```

4. **Run the linters and type checker.**

   ```bash
   ./check-style.sh
   ```

5. **Make your changes and commit.**
   Create a branch, make changes, and push to GitHub.

   ```bash
   git checkout -b my-feature
   git commit -am "Describe your change"
   git push origin my-feature
   ```

6. **Submit a pull request.**
   Open a PR on GitHub and describe the motivation and scope of your change.


## Details

**Style**: We conform to PEP-8 and where that is silent we follow the
[Google style guide](https://google.github.io/styleguide/pyguide.html).
We also use type hints.

Style is enforced with `black`, type-hinting with `mypy`, linting with `pylint`
which is configured to the Google pylintrc (with a few minor adjustments).

To check conformance locally, from within a poetry shell, invoke

```bash
./check-style.sh
```

**Testing**: We use the unittest framework. Tests are all feature tests,
written to validate some user need. Test logic should reflect how a user would
interact with this package. Test names follow the pattern `test_<verb phrase>`
to represent the corresponding user story of "I can [verb phrase]". To run
tests invoke

```bash
poetry run python -m unittest -v          # play all tests
poetry run python -m unittest -v testname # play one test
```

**Continuous Integration**: We use GitHub Actions to automatically run tests
and style checks/linting on every push and pull request to `main`.

**Publishing**: A GitHub Action publishes to PyPI whenever a new version tag is
pushed to `main`. Ensure the version in `pyproject.toml` matches the git tag.

If auto publish fails we can publish manually via
`poetry build; poetry publish`.
Manual publication requires configuring poetry with a PyPI API token.

**Dependency Management**: We use poetry. Common gestures:

```bash
poetry install      # create the virtual environent and install dependencies
poetry env activate # print the command to activate the virtual environment
poetry run COMMAND  # run a command within this environment
code .              # open VS Code within this environment
poetry install -E notebooks # install extra dependencies to use notebooks
poetry add X             # add runtime dependency X
poetry add --group dev X # add development dependency X
```

**Backlog**: A list of pending tasks lives in FUTURE.md.
