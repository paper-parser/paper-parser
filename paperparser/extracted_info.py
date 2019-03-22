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
from .parse import pce, synthesis


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
        self.synth_sentences, self.sent_recor = self.find_synth_sentences(
            self.paper
            )
        self.parsed_spinco = self.parse_for_spinco(self.synth_sentences)
        self.parsed_anneal = self.parse_for_anneal(self.synth_sentences)
        # self.step_order = self.order_steps(self.)

        self.pce_sentences = self.find_pce_sentences(self.paper)
        self.parsed_pce = self.parse_for_pce(self.pce_sentences)

        # Somehow need to associate properties with chemical name...
        self.chem_names_associate = self.magically_extact_chemicals(
            self.paper
            )

        self.relational_dict['Material'] = chemical_name


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











    def extract_synthesis_info(self, flagged_paragraphs):
        # Christine takes synthesis sentence and extracts parameters
        synth_steps_and_param_dict = christines_function(
            flagged_paragraphs['synthesis']
            )

        # Order steps in synthesis
        ordered_step_list = linnettes_function(synthesis_paragraph)
        synth_steps_and_param_dict['step_order'] = ordered_step_list

        self.relational_dict['synthesis'] = synth_steps_and_param_dict


    def extract_performance_metrics(self, flagged_paragraphs):
        performance_dict = {}

        pce_dict = parse_pce(flagged_paragraphs['performance'])
        performance_dict['PCE'] = pce_dict

        ## ECT for other performance metrics...
        # voc_dict = {}
        # voc_dict = parse_voc(flagged_paragraphs['performance'])
        # performance_dict['VOC'] = voc_dict

        # Then put it all back into main ralational dictionary
        self.relational_dict['Performance'] = performance_dict


    def print_ascii_graph(self):
        """ prints ascii graph inspired by the bash git command
            'git log --graph'
            """

        # make_pretty_dict_pretty_in_plain_txt(relational_dict)
        print('Not ready yet, sorry!')



def neels_function(plain_txt):
    """ Probably will be imported from another file

        Flag paragraphs, will be formated as;
        {
            'performance' : [ list of paragraph strings ],
            'synthesis' : [ list of paragraph strings ],
            }

    Sudo code
    ~~~~~~~~~
    for paragraph in plain_txt:
        for sentence in paragraph:
            if sentence about synthesis:
                this paragraph should be flagged as synthesis
            else: pass

            if this sentence talk about performance metric?
                this paragraph flagged as performance
        """

    pass


def christines_function(sentences_or_paragraphs_specific_to_synthesis):
    """ Probably will be imported from another file

        import function 'parse_for_anneal' from Christine's file.

        """

    def parse_for_anneal():
        """ Should be imported from somewhere...

            Returns: dictionary of format:
                synthathis_parameters = {
                    spincoat: [{
                        spd: value,
                        spdunits: units,
                        time: value,
                        timeunits: units,
                        temp: value,
                        tempunits: units
                        }]
                    anneal: [{
                        ...
                        }]
                    ...
                    }
            """
        pass

    synth_txt_list = sentences_or_paragraphs_specific_to_synthesis

    steps_and_parameters_dict = {}
    # Parse for anneal parameters
    for string in synth_txt_list:
        parse_output = parse_for_anneal(synth_txt_list)
        # Add keys to master dictionary if they work,
        # Parsing through each sentence individually doesn't make sense,
        # since we are not taking advantage of CDE's ability to relate
        # across the document.
        if 'spincoat' in parse_output.keys:
            steps_and_parameters_dict['spincoat'] = parse_output['spincoat']
        elif 'anneal' in parse_output.keys:
            steps_and_parameters_dict['anneal'] = parse_output['anneal']

    return steps_and_parameters_dict

def linnettes_function(sentences_or_paragraphs_specific_to_synthesis):
    """ Probably will be imported from another file """
    pass


class PerformanceMetric(object):
    """ Not currently used.
        """

    def __init__(self,
        name,
        value,
        units):
        """
            Args:

                name: string containing name such as; 'PCE', 'VOC', 'JSC', ect

                value: number

                units: string such as; percent, '%', 'V', 'A'
            """
        self.name = name
        self.value = value
        self.units = units

#HJG: Depreciated as of 03/10/19
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class ActiveMaterialGraph(PerformanceMetrics, SynthesisParameters):
#     """ NOTE: Not sure that this is worth doing as implemented. What
#             we probably want is a way to build the component
#             dictionarie. I we should talk about this.


#         Active material extracted from paper and its properties. This
#         class serves as a wrapper for the dictionary structure
#         containing all data and relations extratect from a paper for a
#         single data struction.

#         It will allow access to the data and plotting methods.

#         Example code:

#             amg_1 = ActiveMaterialGraph(
#                 PerformanceMetrics=dict_1,
#                 SynthesisParameters=dict_2,
#                 )

#             # print PCE value and units
#             print(amg_1.PCE.value, amg_1.PCE.units)

#             # print first step in synthesis
#             print(amg_1.synthesis_steps[0])

#         """

#     def __init__(self, chemical_identifier, performace_metrics, synthesis_steps):
#         """
#             take inputs and store into dictionary

#             Args:
#                 performace_metrics: dictionary containing metrics and
#                     associated values. Examaple,
#                         performace_metrics = {
#                             'PCE' : {
#                                 'value' : (number),
#                                 'units' : '%',
#                                 },
#                             'VOC' : {
#                                 'value' : (number),
#                                 'units' : 'V',
#                                 },
#                             'JSC' : {
#                                 'value' : (number),
#                                 'units' : 'A',
#                                 }
#                 synthesis_steps: dictionary containing synthesis steps
#                     and relevant parameters.
#             """


#         # unsure how to do this right now, but what I want is an easy way to build the
#         # Unfinished outline ...

