# My portfolio website made with Jinja2 and Python.

[![Build Status](https://travis-ci.org/rikushoney/rikushoney.com.svg?branch=master)](https://travis-ci.org/rikushoney/rikushoney.com)

## Requirements:
- Python 3.8.0 (I use [pyenv](https://github.com/pyenv/pyenv) to manage my Python versions)
- pip
- (optional, but recommended) [pipenv](https://pipenv.readthedocs.io)

## Install:
### pipenv (recommended):
- ``pipenv install``

### pip:
- Create virtualenv ``python3 -m venv .venv``
- Source virtualenv ``source .venv/bin/activate``
- Install packages ``pip install -e .``

If using pipenv, prepend all following commands with ``pipenv run`` or run them in a ``pipenv shell``

## Building:
Places website in ``out`` folder by default.
- ``website build``

## Live debug server:
Spawning a live server automatically builds and rebuilds the website when changes are detected.
- ``website live``
