"""
paperparser.parse.synthesis
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Built on top of ChemDataExtractor's parse methods.

Parses synthetic parameters from given text containing said parameters
in a disorganized format (e.g. from the text of a paper.) Synthesis parameters
are related to spin-coating and the involved process(es).


DEVELOP NOTES:

HJG 03/10/19:
    Added missing ')' on line 63

"""

# Imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging
import re

from chemdataextractor import Document
from chemdataextractor.model import Compound, BaseModel, \
                                    StringType, ListType, ModelType
from chemdataextractor.doc import Paragraph, Heading
from chemdataextractor.parse import R, I, W, Optional, merge, ZeroOrMore, OneOrMore
from chemdataextractor.parse.cem import chemical_name
from chemdataextractor.parse.base import BaseParser
from chemdataextractor.utils import first


# Define a new class for spin-coating parameters
class SpinCoat(BaseModel):
    """
    Class for spin-coating speeds.
    """
    value = StringType() # perhaps rename if time is collected here too
    units = StringType()
    # time = StringType()
    # timeunits = StringType

# Associate the spin-coating class with a given compound.  May be worth
# getting rid of for our eventual implementation, not yet sure.
Compound.spin_coat_steps = ListType(ModelType(SpinCoat))

# Extract units method from ir.py: find units in the text
def extract_units(tokens, start, result):
    """Extract units from bracketed after nu"""
    for e in result:
        for child in e.iter():
            if 'rpm' or 'r.p.m.' or 'r.p.m' or 'rcf' or 'r.c.f.' in child.text:
                return [E('units', 'whatever the unit is')]
    return []

# Account for extraneous surrounding characters
delim = R('^[;:,\./]$').hide()
solvent = (I('GBL') | R('γ-[Bb]utyrolactone' | chemical_name('solvent')))


# Defining
units = Optional(R(u'^\b?r(\.)?p(\.)?m(\.)?\b?$') | R(u'^r(\.)?c(\.)?f(\.)?$') | R(u'^([x×]?)(\s?)?g$'))(u'units')
#Optional(W('/')).hide() + W(u'^r\.?p\.?m\.?')
#R('^(re)?crystalli[sz](ation|ed)$', re.I)
value = R(u'^\d+(,\d+)?$')(u'value')
spinspd = (value + units)(u'spinspd')

class SpinCoatParser(BaseParser):
    root = spinspd

    def interpret(self, result, start, end):
        compound = Compound(
            spin_coat_steps=[
                SpinCoat(
                    #solvent=first(result.xpath('./solvent/text()')),
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        yield compound

Paragraph.parsers = [SpinCoatParser()]

# Similarly, parse spincoat times
class SpinTime(BaseModel):
    """
    Class for spin-coating step times.
    """
    value = StringType()
    units = StringType()

Compound.spin_coat_times = ListType(ModelType(SpinCoat))
units = combinations of relevant strings
value = define value formats
spintime = (value + units)(u'spintime')

class SpinTimeParser(BaseParser):
    root = spintime
    def interpret(self, result, start, end):
        compound = Compound(
            spin_coat_times=[
                SpinCoat(
                    #solvent=first(result.xpath('./solvent/text()')),
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        yield compound

# Similarly, parse temperatures (e.g. annealing)
class Anneal(BaseModel):
    """
    Class for annealing parameters for perovskite films.
    """
    T = StringType()
    unitsT = StringType()
    time = StringType()
    unitst = StringType()

associate with Compound
define variables
create anneal master variable

create AnnealParser class

# If time: write parser for actual synthesis.  This is tougherself.
# May require methods outside of CDE.
