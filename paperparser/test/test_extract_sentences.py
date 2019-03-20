import chemdataextractor
from ..read_paper import extract_sentences


def test_read_html_paper():
    """Test function for opening a html file and storing it as a Document"""
    
    doc = extract_sentences.read_html_paper(
        '../../development_notebooks/journal_articles/Paper0.html')
    
    assert type(doc) == chemdataextractor.doc.document.Document,\
    'output is not a chemdataextractor Document type'
    
    return


def test_extract_all_sentences():
    """Test function for extracting sentences from a Document"""
    
    doc = extract_sentences.read_html_paper(
        '../../development_notebooks/journal_articles/Paper0.html')
    sentences_list, sentences_record =\
        extract_sentences.extract_all_sentences(doc)
    
    assert type(sentences_list) == list,\
    'sentences_list is not a list'
    assert type(sentences_list[0]) == str,\
    'elements in list are not strings'
    assert len(sentences_list) == 851,\
    'number of strings in list is incorrect'
    assert type(sentences_record) == list,\
    'sentences_record is not a list'
    assert type(sentences_record[0]) == tuple,\
    'elements in liust are not tuples'
    assert len(sentences_record) == 851,\
    'number of tuples in list is incorrect'
    assert sentences_record[3][0] == 2,\
    'paragraph index stored is incorrect'
    assert sentences_record[3][1] ==1,\
    'sentence index stored is incorrect'
    
    return


def test_extract_sentences_given_tag():
    """Test function for extracting sentences from a Document into two separate lists,
    based on given paragraph(s) """
    
    doc = extract_sentences.read_html_paper(
        '../../development_notebooks/journal_articles/Paper0.html')
    sen_yes_arr, sen_no_arr =\
        extract_sentences.extract_sentences_given_tag(doc, [109])
    
    assert type(sen_yes_arr) == list, 'first output is not a list'
    assert type(sen_no_arr) == list, 'second output is not a list'
    assert len(sen_yes_arr) == 12,\
    'number of strings in first list is incorrect'
    assert type(sen_yes_arr[0]) == chemdataextractor.doc.text.Sentence,\
    'elements in first list are not chemdataextractor Sentences'
    assert type(sen_no_arr[0]) == chemdataextractor.doc.text.Sentence,\
    'elements in second list are not chemdataextractor Sentences'
    assert str(sen_yes_arr[11]) == \
    'The active area of this electrode was fixed at 0.16 cm2.',\
    'elements in second output list is incorrect'
    assert str(sen_no_arr[1]) == 'Cookie Notice',\
    'elements in second output list is incorrect'
    
    return