#!/bin/bash
# Called from pre-commit. Run pylint on all python files in the current directory
python -m pylint "$@"
