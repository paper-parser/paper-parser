"""
paperparser.parse.spincoat
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Built on top of ChemDataExtractor's parse methods.

Parses synthetic parameters from given text containing said parameters
in a disorganized format (e.g. from the text of a paper.) Synthesis parameters
are related to spin-coating and the involved process(es).

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


# Creating SpinStep and SpinCoat class, (eventually) with various properties:
# speed and speed units (for now), other parameters in the future.
class SpinStep(BaseModel):
    """
    Class containing properties for each spin-coating step.
    """
    spd = StringType()
    spdunits = StringType(contextual=True) # have not yet figured this out
    #time = StringType()
    #timeunits = StringType()
    #temp = StringType()
    #tempunits = StringType()

class SpinCoat(BaseModel):
    """
    Class for full list of spin-coating steps for entire spin-coating process.
    """
    solvent = StringType(contextual=True)
    steps = ListType(ModelType(SpinStep))
    #spd = StringType()
    #spdunits = StringType()

# Associate the spin-coating class with a given compound.  May be worth
# getting rid of for our eventual implementation, not yet sure.
Compound.spin_coat = ListType(ModelType(SpinCoat))

# Account for extraneous surrounding characters
gbl = (I('GBL') | R('^γ-?[bB]?utyrolactone$'))
solvent = (gbl | chemical_name)('solvent').add_action(join)


# Variable assignments
# Deliminator
delim = R('^[;:,\./]$').hide()

# Defining formats for spin-coating value and units
spdunits = Optional(R(u'^r(\.)?p(\.)?m(\.)?$') | R(u'^r(\.)?c(\.)?f(\.)?$') | R(u'^([x×]?)(\s?)?g$'))(u'spdunits').add_action(merge)
spd = (Optional(W('(')).hide() + R(u'^\d+(,\d+)[0][0]$')(u'spd') + Optional(W(')')).hide())

step = (spd + ZeroOrMore(spdunits))('step')
steps = (step + ZeroOrMore(ZeroOrMore(delim | W('and')).hide() + step))('steps')

spincoat = (steps + Optional(delim))

class SpinCoatParser(BaseParser):
    root = spincoat

    def interpret(self, result, start, end):
        c = Compound()
        s = SpinCoat(
            solvent=first(result.xpath('./solvent/text()'))
        )
        spdunits = first(result.xpath('./spdunits/text()'))
        for step in result.xpath('./steps/step'):
            spin_step = SpinSpd(
                spd=first(spd_result.xpath('./spd/text()')),
                spdunits=spdunits
            )
            s.steps.append(spin_step)
        c.spin_coat.append(s)
        yield c

# Add new parsers to CDE native paragraph parsers
Paragraph.parsers = [SpinCoatParser()]

# The function still is not working and does not correctly parse
# the test sentence correctly.  Am working on troubleshooting further.
