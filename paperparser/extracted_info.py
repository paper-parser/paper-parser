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
        'material identifier' : 'ABCD',
            'properties'v : {
            'Performance metrics' : {
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
from parse import parse_pce, parse_synthesis


class ExtractSynthesisPerformance(object):
    """ Performs data extraction from paper
        """

    def __init__(self, paper):
        """ Run components to extract information from paper """

        # convert paper to text...

        # Flag paragraphs, will be formated as;
        # {
        #     'performance' : [ list of paragraph strings ],
        #     'synthesis' : [ list of paragraph strings ],
        #     }
        flagged_paragraphs = neels_function(paper)


        # Christine takes synthesis sentence and extracts parameters
        (anneal_parameters, spincoat_parameters) = christines_function(
            flagged_paragraphs['synthesis']
            )

        # Order steps in synthesis
        ordered_step_list = linnettes_function(synthesis_paragraph)

        # Parse paper for PCE
        pce_info = parse_pce(flagged_paragraphs['performance'])

        # ECT for other performance metrics

        wrapped_info_object = build_realtional_dict
        # ....

    return dictionary_of_relational_results


def neels_function(plain_txt):
    """ Probably will be imported from another file

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
    """ Probably will be imported from another file """
    pass

def linnettes_function(sentences_or_paragraphs_specific_to_synthesis):
    """ Probably will be imported from another file """
    pass


class PerformanceMetric(object):
    """
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


class ActiveMaterialGraph(PerformanceMetrics, SynthesisParameters):
    """ NOTE: Not sure that this is worth doing as implemented. What
            we probably want is a way to build the component
            dictionarie. I we should talk about this.


        Active material extracted from paper and its properties. This
        class serves as a wrapper for the dictionary structure
        containing all data and relations extratect from a paper for a
        single data struction.

        It will allow access to the data and plotting methods.

        Example code:

            amg_1 = ActiveMaterialGraph(
                PerformanceMetrics=dict_1,
                SynthesisParameters=dict_2,
                )

            # print PCE value and units
            print(amg_1.PCE.value, amg_1.PCE.units)

            # print first step in synthesis
            print(amg_1.synthesis_steps[0])

        """

    def __init__(self, chemical_identifier, performace_metrics, synthesis_steps):
        """
            take inputs and store into dictionary

            Args:
                performace_metrics: dictionary containing metrics and
                    associated values. Examaple,
                        performace_metrics = {
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
                                }
                synthesis_steps: dictionary containing synthesis steps
                    and relevant parameters.
            """


        # unsure how to do this right now, but what I want is an easy way to build the
        # Unfinished outline ...

