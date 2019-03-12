"""
paperparser.parse.spincoat
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Built on top of ChemDataExtractor's parse methods.

Parses spin-coating parameters from given text containing said parameters
in a disorganized format (e.g. from the text of a paper).  Returns organized
format for the parameters.

"""

# Imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re

from chemdataextractor import Document
from chemdataextractor.model import Compound, BaseModel, \
                                    StringType, ListType, ModelType
from chemdataextractor.doc import Paragraph, Sentence
from chemdataextractor.parse.actions import join
from chemdataextractor.parse import R, I, W, Optional, merge, ZeroOrMore
from chemdataextractor.parse.base import BaseParser
from chemdataextractor.utils import first


# Creating SpinStep and SpinCoat class with various properties:
# speed, time, temperature, and respective units.
class SpinSpd(BaseModel):
    """
    Class for each spin-coating speed in a spin-coating process.
    """
    spdvalue = StringType()
    spdunits = StringType(contextual=True)

class SpinTime(BaseModel):
    """
    Class for each spin-coating time in a spin-coating process.
    """
    timevalue = StringType()
    timeunits = StringType(contextual=True)

class SpinCoat(BaseModel):
    """
    Class for full list of spin-coating step parameters for full process.
    """
    #solvent = StringType(contextual=True)
    spds = ListType(ModelType(SpinSpd))
    times = ListType(ModelType(SpinTime))

# Associate the spin-coating class with a given compound.  May be worth
# getting rid of for our eventual implementation, not yet sure.
Compound.spin_coat = ListType(ModelType(SpinCoat))

# Variable assignments
# Deliminators -- hide from tokenization
delim = R('^[;:,\./]$').hide()

# Defining formats for spin-coating value and units
spdunits = (R(u'^r(\.)?p(\.)?m(\.)?$') | R(u'^r(\.)?c(\.)?f(\.)?$') | R(u'^([x×]?)(\s?)?g$'))('spdunits').add_action(join) + ZeroOrMore(delim)
spdvalue = Optional(W('(')).hide() + R(u'^\d+(,\d+)[0][0]$')('spdvalue') + Optional(W(')')).hide()

# Defining formats for spin-coating time and time units
timeprefix = I('for').hide()
timeunits = (R('^s?(ec|econds)?$') | R('^m?(in|inute)?(s)?$') | R('^h?(ou)?(r)?(s)?$'))('timeunits').add_action(join) + Optional(delim)
timevalue = R('^\d{,3}$')('timevalue') + Optional(delim) #<3 digits

# Putting everything together
spdprefix = I('at').hide()
spd = (spdvalue)('spd')
spds = (spd + ZeroOrMore(ZeroOrMore(delim | W('and')).hide() + spd))('spds')
time = (timevalue)('time')
times = (time + ZeroOrMore(ZeroOrMore(delim | W('and')).hide() + time))('times')

# Format for string containing spin-coat information
spincoat = (Optional(spdprefix) + spds + Optional(delim) + Optional(spdunits) + Optional(delim) + Optional(timeprefix) + Optional(delim) + times + Optional(delim) + Optional(timeunits) + Optional(delim))('spincoat')

# New parser class for spin-coat parameter parsing
class SpinCoatParser(BaseParser):
    """
    Parser class for parsing spin-coating parameters.
    """
    root = spincoat

    def interpret(self, result, start, end):
        c = Compound()
        s = SpinCoat(
        #    solvent=first(result.xpath('./solvent/text()'))
        )
        spdunits = first(result.xpath('./spdunits/text()'))
        timeunits = first(result.xpath('./timeunits/text()'))
        for spd in result.xpath('./spds/spd'):
            spin_spd = SpinSpd(
                spdvalue=first(spd.xpath('./spdvalue/text()')),
                spdunits=spdunits
            )
            s.spds.append(spin_spd)
        for time in result.xpath('./times/time'):
            spin_time = SpinTime(
                timevalue=first(time.xpath('./timevalue/text()')),
                timeunits=timeunits
            )
            s.times.append(spin_time)
        c.spin_coat.append(s)
        yield c

# Add new parsers to CDE native paragraph parsers
#Paragraph.parsers = [SpinCoatParser()]

# Define function to accept sentence and parse using the above parser
def parse_spincoat(spincoat_str):
    """
    Given a string as input, converts the string into a ChemDrawExtractor
    Paragraph and returns a list of spin-coating parameters (speeds and times)
    found via parsing the string.
    """
    Sentence.parsers = [SpinCoatParser()]
    return Sentence(spincoat_str).records.serialize()
