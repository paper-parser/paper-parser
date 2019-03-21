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
from chemdataextractor.doc import Paragraph

# From my ipynb ...
class Pce(BaseModel):
    value = StringType()
    units = StringType()

Compound.pce = ListType(ModelType(Pce))

prefix = (
    I(u'PCEs')
    |
    I(u'pce')
    |
    I(u'power')
    +
    I(u'conversion')
    +
    I(u'efficiency')
    ).hide()
common_text = R('\D').hide()
units = (W(u'%') | I(u'percent'))(u'units')
# value = R(u'^\d+(\.\d+)?$')(u'value')
value = R(u'\d+(\.\d+)?')(u'value')
pce = (
    prefix
    +
    Optional(common_text)
    +
    Optional(common_text)
    +
    Optional(common_text)
    +
    value
    +
    units
    )(u'pce')


class PceParser(BaseParser):
    root = pce

    def interpret(self, result, start, end):
        compound = Compound(
            pce=[
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

    pass
