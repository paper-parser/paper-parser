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

from chemdataextractor.model import Compound, UvvisSpectrum, UvvisPeak, BaseModel
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

Compound.pce = ListType(ModelType(PCE))

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
                PCE(
                    value=first(result.xpath('./value/text()')),
                    units=first(result.xpath('./units/text()'))
                )
            ]
        )
        yield compound


# Paragraph.parsers.append(PCEParser())

# end of working model for parser...

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# From here down still equivilent to 'chemdataextractor.parse.uvvis'
# log = logging.getLogger(__name__)


# delim = R('^[;:,\./]$').hide()

# solvent = chemical_name('solvent')
# units = Optional(W('/')).hide() + W('nm')('units')
# value = R('^\d{3,4}(\.\d+)?\.?$')('value').add_action(strip_stop)
# shape = R('^(m|medium|w|weak|s|strong|n|narrow|b|broad|sh|sharp)$', re.I)('shape') + Optional(I('peak')).hide()
# peak_meta_options = shape
# peak_meta = W('(').hide() + peak_meta_options + ZeroOrMore(delim + peak_meta_options) + W(')').hide()
# insolvent = T('IN') + solvent
# uvvis_abs_title = (
#     I('absorption') + R('max(ima)?') |
#     R('^λ(a(bs)?|max)$') + ZeroOrMore(R('^a?max$', re.I) | R('abs(or[bp]tion)?', re.I) | I('a') | W(',')) |
#     W('λ$') + OneOrMore(R('^a?max$', re.I) | R('abs(or[bp]tion)?', re.I) | I('a') | W(',')) |
#     R('uv([-/]?vis)?', re.I) |
#     I('UV') + hyphen + R('^vis(ible)?$', re.I) + Optional(R('^abs(or[bp]tion)?$'))
# )
# prelude = uvvis_abs_title.hide() + Optional(delim) + Optional(I('data')) + Optional(insolvent) + Optional(delim) + Optional(units)
# peak = (value + Optional(peak_meta))('peak')
# peaks = (peak + ZeroOrMore(ZeroOrMore(delim | W('and')).hide() + peak))('peaks')
# uvvis = (prelude + peaks + Optional(delim) + Optional(units) + Optional(insolvent))('uvvis')


# class UvvisParser(BaseParser):
#     """"""
#     root = uvvis

#     def interpret(self, result, start, end):
#         c = Compound()
#         u = UvvisSpectrum(
#             solvent=first(result.xpath('./solvent/text()'))
#         )
#         units = first(result.xpath('./units/text()'))
#         for peak_result in result.xpath('./peaks/peak'):
#             uvvis_peak = UvvisPeak(
#                 value=first(peak_result.xpath('./value/text()')),
#                 units=units,
#                 shape=first(peak_result.xpath('./shape/text()'))
#             )
#             u.peaks.append(uvvis_peak)
#         c.uvvis_spectra.append(u)
#         yield c
