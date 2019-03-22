import chemdataextractor
from chemdataextractor import Document
from chemdataextractor.reader import HtmlReader
import numpy as np

def extract_sentences(paper_path, para_yes):
    """extracts sentences from a paper into two lists, given that para_yes contains
    a list of document element numbers corresponding to paragraphs manually identified
    as those containing synthesis information"""

    f = open(paper_path, 'rb')
    doc = Document.from_file(f, readers=[HtmlReader()])

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
