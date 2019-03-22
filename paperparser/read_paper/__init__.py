"""
paperparser.parse
~~~~~~~~~~~~~~~~~

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