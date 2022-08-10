=========
Trade Bot
=========

Setup
======

**Requirements:**
- Python 3.8 >
- Poetry (package manager)

**Running for the first time:**
1. Run `poetry install`.
2. If on VSCode, set your interpreter (i.e. `cmd/ctrl + shift + x`` -> install "Python" -> `cmd/ctrl + shift + p`` -> then type "Python: Select Interpreter") to the one set by Poetry.
3. Run `pre-commit install` to set up your pre-commit hooks.
4. Run `poe dev` to start the development environment. This should automatically re-run after you make any code changes.

Contributing
============

1. Run `git pull` from the `development` branch and do a `git checkout -b {my_branch_name}` to open a local side branch.
2. Commit (e.g. `git add` and `git commit`) all your work in that side branch.
3. Run `git push` after completing work in the side branch.
4. Open a pull request (for the `development` branch) on Github. Your code will be reviewed and subject to changes.
5. Once your pull request is approved, please merge your branch to `development`
