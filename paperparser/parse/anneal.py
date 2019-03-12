"""
paperparser.parse.anneal
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Built on top of ChemDataExtractor's parse methods.

Parses annealing parameters from given text containing said parameters
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

# Creating Anneal class with various subclasses: AnnealTemp and AnnealTime
#(for parsing temperature and time, respectively).
class AnnealTemp(BaseModel):
    """
    Class for each spin-coating speed in a spin-coating process.
    """
    tempvalue = StringType()
    tempunits = StringType(contextual=True)

class AnnealTime(BaseModel):
    """
    Class for each spin-coating time in a spin-coating process.
    """
    timevalue = StringType()
    timeunits = StringType(contextual=True)

class Anneal(BaseModel):
    """
    Class for full list of spin-coating step parameters for full process.
    """
    temps = ListType(ModelType(AnnealTemp))
    times = ListType(ModelType(AnnealTime))

# Associating anneal parameters with a chemical object
Compound.anneal = ListType(ModelType(Anneal)) # currently not working

# Defining object parameters for the AnnealParser parser
# Deliminators
delim = R('^[;:,\./]$').hide()

# Defining formats for annealing temperature and units
tempprefix = I('at').hide()
tempunits = (W('°') + R('^[CFK]\.?$'))('tempunits').add_action(merge)
tempvalue = R('^\d{2,4}?$')('tempvalue').add_action(merge) + Optional(delim)

# Defining formats for spin-coating time and time units
timeprefix = I('for').hide()
timeunits = (R('^s?(ec|econds)?$') | R('^m?(in|inute)?(s)?$') | R('^h?(ou)?(r)?(s)?$'))('timeunits').add_action(join) + Optional(delim)
timevalue = R('^\d{,2}$')('timevalue') + Optional(delim)

# Putting everything together
temp = (tempvalue)('temp')
temps = (temp + ZeroOrMore(ZeroOrMore(delim | W('and')).hide() + temp))('temps')
time = (timevalue)('time')
times = (time + ZeroOrMore(ZeroOrMore(delim | W('and')).hide() + time))('times')

# Parses anneal parameters from a sentence of this specific format:
# "at [temp] [tempunits] for [time] [timeunits]"
annealing = (tempprefix + temps + Optional(delim) + tempunits + Optional(delim) + timeprefix + Optional(delim) + times + Optional(delim) + timeunits + Optional(delim))('annealing')

# Define new parsing class for parsing annealing parameters
class AnnealParser(BaseParser):
    root = annealing

    def interpret(self, result, start, end):
        c = Compound()
        s = Anneal()
        tempunits = first(result.xpath('./tempunits/text()'))
        timeunits = first(result.xpath('./timeunits/text()'))
        for temp in result.xpath('./temps/temp'):
            anneal_temp = AnnealTemp(
                tempvalue=first(temp.xpath('./tempvalue/text()')),
                tempunits=tempunits
            )
            s.temps.append(anneal_temp)
        for time in result.xpath('./times/time'):
            anneal_time = AnnealTime(
                timevalue=first(time.xpath('./timevalue/text()')),
                timeunits=timeunits
            )
            s.times.append(anneal_time)
        c.anneal.append(s)
        yield c

# Apply annealing parser designed above to a given paragraph
#Sentence.parsers = [AnnealParser()]

def parse_anneal(anneal_str):
    """
    Given a string as input, converts the string into a ChemDrawExtractor
    Sentence and returns a list of annealing parameters (temperatures and
    times) found via parsing the string.
    """
    Sentence.parsers = [AnnealParser()]
    return Sentence(anneal_str).records.serialize()
