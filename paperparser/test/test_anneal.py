# Import(s)
from chemdataextractor.doc import Sentence
from paperparser.parse.anneal import AnnealParser, annealing, parse_anneal


# Test variables and outputs
test_s = "The substrate was then dried on a hot plate at 100 °C or 150 °C for 10 min."
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
        assert isinstance(test_s_output[0], dict), \
        'Error: output must be list of dictionaries'
    except IndexError:
        raise Exception('Error: output is not a list, or is an empty list')
    except TypeError:
        raise Exception('Error: output must be a list of dictionaries')
