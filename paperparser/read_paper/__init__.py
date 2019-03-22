"""
paperparser.read_paper
~~~~~~~~~~~~~~~~~~~~~~

    read_paper
    |\
    | extract_sentences: Wrapper for CDE tool for extracting sentences
    |     from a paper in .html format.
    |\
    | search_paper_for_perform_sentences: Tools for searching paper
    |     for sentences containing quantitative performance metric
    |     information
     \
      sentence_classifier: Tools for working with SVM classifier for
          extracting sentences about synthesis


Built on top of ChemDataExtractor version 1.3.0, copyright 2017 Matt
Swain and contributors.
github repo: .../mcs07/ChemDataExtractor/

    """
# Imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


from .extract_sentences import read_html_paper, extract_all_sentences,\
                                extract_sentences_given_tag
from .search_paper_for_perform_sentences import sentence_list_from_paper,\
                                quantified_performance_sentence_search,\
                                list_perform_sents
from .sentence_classifier import clean_text, spacy_tokenizer, train_predictor,\
                                classify_sentences
