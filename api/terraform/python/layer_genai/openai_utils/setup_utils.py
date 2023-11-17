# -*- coding: utf-8 -*-
"""Lawrence McDaniel https://lawrencemcdaniel.com."""
# pylint: disable=open-builtin
import io
import os
import re
from typing import Dict

HERE = os.path.abspath(os.path.dirname(__file__))

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))


def load_version() -> Dict[str, str]:
    """Stringify the __about__ module."""
    version: Dict[str, str] = {}
    with io.open(os.path.join(HERE, "__version__.py"), "rt", encoding="utf-8") as f:
        exec(f.read(), version)  # pylint: disable=exec-used
    return version


VERSION = load_version()


def get_semantic_version() -> str:
    """
    Return the semantic version number.

    Example valid values of __version__.py are:
    0.1.17
    0.1.17-next.1
    0.1.17-next.2
    0.1.17-next.123456
    0.1.17-next-major.1
    0.1.17-next-major.2
    0.1.17-next-major.123456

    Note:
    - pypi does not allow semantic version numbers to contain a dash.
    - pypi does not allow semantic version numbers to contain a 'v' prefix.
    - pypi does not allow semantic version numbers to contain a 'next' suffix.
    """
    version = VERSION["__version__"]
    version = re.sub(r"-next\.\d+", "", version)
    return re.sub(r"-next-major\.\d+", "", version)
