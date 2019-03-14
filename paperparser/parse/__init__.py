"""
paperparser.parse
~~~~~~~~~~~~~~~~~

Module containing tootls to parse synthesis parameters and PCE (power
conversion efficiency) from perovskite paper text.

Built on top of ChemDataExtractor version 1.3.0, copyright 2017 Matt
Swain and contributors.
github repo: .../mcs07/ChemDataExtractor/

"""
# External Imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from chemdataextractor import parse

 # Function Imports
 from .spincoat import parse_spincoat
 from .anneal import parse_anneal

# Parser imports
from .spincoat import SpinCoatParser
from .anneal import AnnealParser
from .pce import PceParser
