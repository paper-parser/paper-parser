"""
paperparser.test.test_extracted_info
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Test functions for paperparser.extracted_info
"""
# Imports
import chemdataextractor as cde

from paperparser import extracted_info
from paperparser.parse import anneal, order, pce, spincoat
from paperparser.read_paper import extract_sentences,\
                                    search_paper_for_perform_sentences,\
                                    sentence_classifier

# Tests begin here
class TestSynthesisAndPerformanceSummary(object):
    """
        """

    def setUp(self):
        """ Run components to extract information from paper """

        # Load paper


    def test_summarize(self):

        assert True == False, "Write the test dumbo"


    def test_read_paper(self):

        assert True == False, "Write the test dumbo"

    def test_find_synth_sentences(self):

        assert True == False, "Write the test dumbo"


    def test_classify_sents(self):

        assert True == False, "Write the test dumbo"


    def test_parse_for_spinco(self):

        assert True == False, "Write the test dumbo"


    def test_parse_for_anneal(self):

        assert True == False, "Write the test dumbo"



    def test_find_pce_sentences(self):

        assert True == False, "Write the test dumbo"



    def test_parse_for_pce(self):

        assert True == False, "Write the test dumbo"


    def test_print_ascii_graph(self):
        """
        Test function for print_ascii_graph;
        Currently empty as the function to be tested has not been written.
        """
        assert True, "Write the test dumbo"


    def test_magically_extract_chemicals(self):
        """
        Test function for magically_extract_chemicals;
        Currently empty as the function to be tested has not been written.
        """
        assert True, "Write the test dumbo"
