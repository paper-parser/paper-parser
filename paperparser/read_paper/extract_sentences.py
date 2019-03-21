import chemdataextractor
from chemdataextractor import Document
from chemdataextractor.reader import HtmlReader
import numpy as np
import os

def read_html_paper(paper_path):
    """Opens a HTML paper and stores it as a chemdataextractor Document"""
   
    f = open(paper_path, 'rb')
    doc = Document.from_file(f, readers=[HtmlReader()])

    return doc


def extract_all_sentences(doc):
    """Extracts all sentences in paragraphs in paper as a list of strings.
    Keeps track of paragraph index and sentence index as a list of tuples
    in output sentences_record."""

    sentences_list = list()
    sentences_record = list()

    for i in range(len(doc.elements)):
        # loop through indicies of document elements in CDE Document
        # object.
        if type(doc.elements[i]) == chemdataextractor.doc.text.Paragraph:
            sen_index = 0
            for sentence in doc.elements[i]:
                sentences_list.append(str(sentence))
                sentences_record.append((i, sen_index))
                sen_index = sen_index + 1

    return sentences_list, sentences_record


def extract_sentences_given_tag(doc, para_yes):
    """extracts sentences from a paper into two lists, given that para_yes
    contains a list of document element numbers corresponding to paragraphs
    manually identified as those containing synthesis information"""

    sen_yes_arr = list()
    sen_no_arr = list()

    elem_all = np.arange(0,len(doc))
    para_no = np.delete(elem_all, para_yes)

    for i in para_no:
        if type(doc.elements[i]) == chemdataextractor.doc.text.Paragraph:
            for sentence in doc.elements[i]:
                sen_no_arr.append(sentence)

    for i in para_yes:
        if type(doc.elements[i]) == chemdataextractor.doc.text.Paragraph:
            for sentence in doc.elements[i]:
                sen_yes_arr.append(sentence)

    return sen_yes_arr, sen_no_arr