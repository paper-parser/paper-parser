# -*- coding: utf-8 -*-
"""
PaperParser
~~~~~~~~~~~
package structure:

    paperparser:
    |
    |\
    | parse:
    | |\
    | | anneal
    | |\
    | | order
    | |\
    | | pce
    |  \
    |   spincoat
    |
    |\
    | read_paper
    | |\
    | | extract_sentences
    | |\
    | | search_paper_for_perform_sentences
    |  \
    |   sentence_classifier
    |
    |\
    | extracted_info
    |
    test


"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import logging


__title__ = 'PaperParser'
__version__ = '1.0.0'
__author__ = 'Christine Chang, Harrison Goldwyn, Linnette Teo, and Neel Shah'
__license__ = 'MIT'
__copyright__ = 'Copyright 2019 PaperParser team'
__status__ = 'Not ready'

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())