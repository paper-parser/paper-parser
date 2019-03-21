"""
paperparser.parse.pce
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is built on top of the chemdataextractor module:
'chemdataextractor.parse.uvvis' as an example for implementaion of the
chemdataextractor pasing syntax.

Parses Power conversion efficiency and related perovskite device
information from conclusive text at the end of a scientific paper.

"""

# from __future__ import absolute_import
# from __future__ import division
# from __future__ import print_function
# from __future__ import unicode_literals
import logging
import re

from chemdataextractor.model import Compound, UvvisSpectrum, UvvisPeak, BaseModel, StringType, ListType, ModelType
from chemdataextractor.parse.common import hyphen
from chemdataextractor.parse.base import BaseParser
from chemdataextractor.utils import first
from chemdataextractor.parse.actions import strip_stop
from chemdataextractor.parse.elements import W, I, T, R, Optional, ZeroOrMore, OneOrMore
from chemdataextractor.parse.cem import chemical_name
from chemdataextractor.doc import Paragraph, Sentence

# From my ipynb ...
class Pce(BaseModel):
    value = StringType()
    units = StringType()

Compound.pce_pattern = ListType(ModelType(Pce))

abbrv_prefix = (
    I(u'PCE') | I(u'PCEs') | I(u'pce') ).hide()
words_pref = (
    I(u'power') + I(u'conversion') + I(u'efficiency')
    ).hide()
hyphanated_pref =(
    I(u'power-conversion') + I(u'efficiency')
    ).hide()
prefix = abbrv_prefix | words_pref | hyphanated_pref

common_text = R('(\w+)?\D(\D+)+(\w+)?').hide()
units = (W(u'%') | I(u'percent'))(u'units')
# value = R(u'^\d+(\.\d+)?$')(u'value')
value = R(u'\d+(\.\d+)?')(u'value')

pce_first= (
    prefix + ZeroOrMore(common_text) + value + units
    )(u'pce')
pce_second = (
    value + units + prefix)(u'pce')

pce_pattern = pce_first | pce_second

class PceParser(BaseParser):
    root = pce_pattern

    def interpret(self, result, start, end):
        compound = Compound(
            pce_pattern=[
                Pce(
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        yield compound



def parse_pce(list_of_sentences):
    """ Takes a list of sentences and parses for quantified PCE
        information and relationships to chemicals/chemical labels
        """

    Sentence.parsers.append(PceParser())

    cde_senteces = [Sentence(sent).records.serialize() for sent in list_of_sentences]
    return cde_senteces
