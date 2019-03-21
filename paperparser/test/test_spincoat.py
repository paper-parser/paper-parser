# Import(s)
from ..parse import spincoat # not sure how to write this correctly
from chemdataextractor.doc import Sentence

# Test variables and outputs
test_s = Sentence(u'The resulting solution was coated onto the mp-TiO2/bl-TiO2/FTO substrate by a consecutive two-step spin-coating process at 1,000 and 5,000 r.p.m for 10 and 20 s, respectively.')
test_s_output = spincoat.parse_spincoat(test_s)

# Test functions
def test_parse_spincoat():
    """
    Test function for spincoat.parse_spincoat
    """
    assert isinstance(test_s, str), 'Incorrect input type: string required'
    assert isinstance(test_s_output, list), (
        'Error: incorrect output type (list expected)'
        )
    assert test_s_output, 'Error: no parameters detected (parsing error)'
    try:
        assert isinstance(test_s_output[0], dict), \
        'Error: output must be list of dictionaries')
    except IndexError:
        raise Exception('Error: output is not a list, or is an empty list')
    except TypeError:
        raise Exception('Error: output must be a list of dictionaries')
