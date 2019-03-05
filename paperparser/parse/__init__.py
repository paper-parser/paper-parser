"""
paperparser.parse
~~~~~~~~~~~~~~~~~~~~~

Module containing tootls to parse synthesis parameters and pce from
perovskite paper text.

Built on top of ChemDataExtractor version 1.3.0, copyright 2017 Matt
Swain and contributors.
github reop: ...

"""

from chemdataextractor import parse

from .pce import PCEParser
from .synthesis import SynthesisParser
