"""
paperparser.test.test_spincoat
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Test function for the spin-coating parameters parser
(paperparser.parse.spincoat).

Future work: implement a test class.
"""

# Import(s)
from chemdataextractor.doc import Sentence
from paperparser.parse.spincoat import SpinCoatParser, spincoat, parse_spincoat


# Test variables and outputs
test_s = 'The resulting solution was coated onto the mp-TiO2/bl-TiO2/FTO substrate by a consecutive two-step spin-coating process at 1,000 and 5,000 r.p.m for 10 and 20 s, respectively.'
test_s_output = parse_spincoat(test_s)


# Test functions
def test_parse_spincoat():
    """
    Test function for spincoat.parse_spincoat.
    """
    assert isinstance(test_s, str), 'Incorrect input type: string required'
    assert isinstance(test_s_output, list), \
        'Error: incorrect output type (list expected)'
    assert test_s_output, 'Error: no parameters detected (parsing error)'
    try:
        level0 = test_s_output[0]
        level1 = test_s_output[0].get('spin_coat')[0]
        level2a = test_output[0].get('spin_coat')[0].get('spds')[0]
        level2b = test_s_output[0].get('spin_coat')[0].get('times')[0]
        assert isinstance(level0, dict), \
            'Error: output must be list of dictionaries'
        assert 'spin_coat' in level0, \
            'Error: spincoat parameter either not found, or parsed incorrectly'
        assert 'spds' and 'times' in level1, \
            'Error: Spincoat parameters not detected or incorrectly parsed'
        assert 'spdvalue' and 'spdunits' in level2a, \
            'Error: Spincoat speeds not detected or incorrectly parsed'
        assert 'timevalue' and 'timeunits' in level2b, \
            'Error: Spincoat times not detected or incorrectly parsed'
    except IndexError:
        raise Exception('Error: output is not a list, or is an empty list')
    except TypeError:
        raise Exception('Error: output must be a list of dictionaries')
