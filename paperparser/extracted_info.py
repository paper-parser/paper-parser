"""
paperparser.act_mat_graph
~~~~~~~~~~~~~~~~~~~~~~~~~

This file builds the object to be extracted from a scientific paper.

The high level class describes the main component of the PV device with
chemical properties we wish to associate with specific components of
the synthesis. The data will be stored as a dictionary of dictionaries


Example graph representation of material object:

    Material (some chemical name)
    |\
    | Performance metrics
    | |\
    | | VOC - # Volts
    | |\
    | | JSC - # Amps
    | |\
    | | PCE - # percent
    | ect
    |
    Synthesis
    |\
    | step 1 - property
    |  \
    |   other property
    |\
    | step 2 - property
    |  \
    |   property
    |\
    | ect. for other steps...
    |
    step ordering: ['step 1', 'step 2', 'step 3']


In dictionary form (following implementaion):

    object = {
        'Material' : 'ABCD',  # Identifier
            'Properties' : {
                'Performance' : {
                    'PCE' : {
                        'value' : (number),
                        'units' : '%',
                        },
                    'VOC' : {
                        'value' : (number),
                        'units' : 'V',
                        },
                    'JSC' : {
                        'value' : (number),
                        'units' : 'A',
                        },
                    ect...
                    },
                'Synthesis' : {
                    'spincoat' : {
                        'time' : {
                            'value' : (number),
                            'units' : 's',
                            },
                        },
                    'annel' : {
                        'time' : {
                            'value' : (number),
                            'units' : 's',
                            },
                        'temerpature' : {
                            'value' : (number),
                            'units' : 'K',
                            },
                    ect...
                }
            }
        }


Development Notes:

    03/07/19: Changing implementation of 'ActiveMaterialGraph' to take advantage

"""

import sys
from .parse import pce, synthesis
from .read_paper import (
    extract_sentences, sentence_classifier, search_paper_for_perform_sentences
    )

from .parse import anneal, order, spincoat, pce

import pandas as pd
from sklearn.externals import joblib


class SynthesisAndPerformanceSummary(object):
    """ Performs data extraction from paper
        """

    def __init__(self, paper_html_path):
        """ Run components to extract information from paper """

        # convert paper to text...

        self.paper_html_path = paper_html_path

        self.relational_dict = self.summarize(self.paper_html_path)


    def summarize(self):

        self.paper = read_paper(self.paper_html_path)
        self.all_sentences, self.sent_recor = self.find_synth_sentences(
            self.paper
            )
        self.synth_sentences = self.classify_sents(self.all_sentences)
        self.parsed_spinco = self.parse_for_spinco(self.synth_sentences)
        self.parsed_anneal = self.parse_for_anneal(self.synth_sentences)
        # self.step_order = self.order_steps(self.)

        self.pce_sentences = self.find_pce_sentences(self.paper)
        self.parsed_pce = self.parse_for_pce(self.pce_sentences)

        # Somehow need to associate properties with chemical name...
        self.chem_names_associate = self.magically_extact_chemicals(
            self.paper
            )

        self.relational_dict = {
            'Parsed_Spincoat' : self.parsed_spinco,
            'Parsed_Anneal' : self.parsed_anneal,
            'Parsed_PCE' : self.parsed_pce,
            }


    def read_paper(self, paper_html_path):

        paper = extract_sentences.read_html_paper(
            self.paper_html_path
            )

        return paper


    def find_synth_sentences(self, paper):

        (
            X_sentences,
            sentences_record
            ) = extract_sentences.extract_all_sentences(
                self.paper
                    )
        return X_sentences, sentences_record


    def classify_sents(self, sentences):

        syn_sen_model = joblib.load('syn_sen_model.pkl')

        (
            pred_data,
            synthesis_sentences,
            not_synthesis_sentences,
            ) = sentence_classifier.classify_sentences(
                syn_sen_model,
                X_sentences,
                )

        return synthesis_sentences


    def parse_for_spinco(self, synth_sentences):

        spincoat_parse_results = [
            spincoat.parse_spincoat(synth_sentences)
            for synth_sentences in synthesis_sentences
            ]

        return spincoat_parse_results


    def parse_for_anneal(self, synth_sentences):

        anneal_parse_results = [
            anneal.parse_anneal(synth_sentences)
            for synth_sentences in synthesis_sentences
            ]

        return anneal_parse_results


    def find_pce_sentences(self, paper):

        relevant_sentences_to_pce = (
            search_paper_for_perform_sentences.list_perform_sents(
                paper
                )
            )

        return relevant_sentences_to_pce


    def parse_for_pce(self, pce_sentences):

        parsed_pce_info = pce.parse_pce(pce_sentences)

        return parsed_pce_info


    def print_ascii_graph(self):
        """ prints ascii graph inspired by the bash git command
            'git log --graph'
            """

        # make_pretty_dict_pretty_in_plain_txt(relational_dict)
        print('Not ready yet, sorry!')


        self.chem_names_associate = self.magically_extact_chemicals(
            self.paper
            )

    def magically_extact_chemicals(self, paper):
        """
            """
        print('You wish bud!')




















