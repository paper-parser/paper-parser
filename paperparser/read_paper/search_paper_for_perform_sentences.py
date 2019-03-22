""" Contains base functions for proper funtioning of the MASTER
    function of this script:

        list_perform_sents: which takes an html file and by default
            returns the sentences with quantitative information on
            device PCE.

            Args:
                paper_html_file: string including path to paper html
                    file.
                metric: By default the string 'PCE', but can be 'VOC'
                    or 'JSC'. Controlls case insensitive search for
                    metric as well as corresponding numeric information
                    .
    """

import sys
import re

from paperparser.read_paper import extract_sentences


def sentence_list_from_paper(paper_html_file):
    """ Extracts list of sentences from an html file using
        ChemDataExtractor's html reader.
        """

    paper = extract_sentences.read_html_paper('journal_articles/Paper0.html')
    X_sentences, sentences_record = extract_sentences.extract_all_sentences(paper)

    return X_sentences


def quantified_performance_sentence_search(sentence_list, metric='PCE'):
    """ Finds sentences in list that contain quantitative information
        about PCE (power conversion efficiency)
        """

    return_sents = []

    if metric == 'PCE':
        metric_patterns = ['PCE']
        units_patterns = ['%', 'percent']
    elif metric == "VOC":
        metric_patterns = ['VOC']
        units_patterns = ['V\w', 'volts']
    elif metric == "JSC":
        metric_patterns = ['JSC']
        units_patterns = ['A\w', 'amps']
    else:
        raise ValueError('{} is not a valid performance metric'.format(metric))
    for sent in sentence_list:
        for pce_pattern in metric_patterns:
            # Check for pce_pattern
            pce_found = re.search(pce_pattern, sent, re.IGNORECASE)
            if pce_found: # check for percent and stop iterating if found
                # Check for numbers
                numbers_found = re.search('\d+', sent)
                if not numbers_found:
                    # Stop looking at sentence
                    break
                # Check for units
                for pce_units_pattern in units_patterns:
                    units_found = re.search(pce_units_pattern, sent)
                    if units_found: break # stop looking for units
                    # if this loop exits with out finding units, throw away the sentence
                if units_found:
                    return_sents.append(sent)
                    break
    return return_sents


def list_perform_sents(paper_html_file, metric='PCE'):
    """ Wrapper to take html file and return a list of sentences
        containing quantified infromation on specific performance
        metrics (PCE by default).
        """

    all_sentences = sentence_list_from_paper(paper_html_file)
    sentences_w_perf_metric_info = quantified_performance_sentence_search(
        sentence_list=all_sentences,
        metric=metric,
        )

    return sentences_w_perf_metric_info
