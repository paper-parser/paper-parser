"""
paperparser.test.test_anneal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Test function for the annealing parameters parser (paperparser.parse.anneal).

Future work: implement a test class.
"""

# Import(s)
from chemdataextractor.doc import Sentence
from paperparser.parse.anneal import AnnealParser, annealing, parse_anneal


# Test variables and outputs
test_s = "The substrate was dried on a hot plate at 100 °C for 10 min."
test_s_output = parse_anneal(test_s)


# Test functions
def test_parse_anneal():
    """
    Test function for anneal.parse_anneal
    """
    assert isinstance(test_s, str), 'Incorrect input type: string required'
    assert isinstance(test_s_output, list), \
        'Error: incorrect output type (list expected)'
    assert test_s_output, 'Error: no parameters detected (parsing error)'
    try:
        level0 = test_s_output[0]
        level1 = test_s_output[0].get('anneal')[0]
        level2a = test_output[0].get('anneal')[0].get('temps')[0]
        level2b = test_s_output[0].get('anneal')[0].get('times')[0]
        assert isinstance(level0, dict), \
            'Error: output must be list of dictionaries'
        assert 'spin_coat' in level0, \
            'Error: spincoat parameter either not found, or parsed incorrectly'
        assert 'temps' and 'times' in level1, \
            'Error: Anneal parameters not detected'
        assert 'tempvalue' and 'tempunits' in level2a, \
            'Error: Temperature values and units incorrectly parsed'
        assert 'timevalue' and 'timeunits' in level2b, \
            'Error: Time values and units incorrectly parsed'
        assert isinstance(test_s_output[0], dict), \
        'Error: output must be list of dictionaries'
    except IndexError:
        raise Exception('Error: output is not a list, or is an empty list')
    except TypeError:
        raise Exception('Error: output must be a list of dictionaries')
