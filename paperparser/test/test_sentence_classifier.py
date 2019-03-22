import sys
sys.path.insert(0, '../../paperparser/read_paper')
import sentence_classifier

def test_spacy_tokenizer():
    """ Test function for tokenizing a sentence"""
    sentences = [
        'The quick brown fox jumps over the lazy dog .',
        'By Jove , my quick study of lexicography won a prize .',
        'This is a short sentence .'] #sentences has to be str and list is passed so will raise a type error
    try:
        tokenized_sentences = sentence_classifier.spacy_tokenizer(sentences)
    except (AssertionError):
        pass
    else:
        raise Exception ("Exception not handled by Asserts")
    tokenized_sentences_1 = sentence_classifier.spacy_tokenizer(sentences[0])
    assert type(tokenized_sentences_1) == list,\
    """output is ['quick', 'brown', 'fox', 'jump', 'lazy', 'dog'] is to check whether stop words and punctuation is working"""
    assert len(tokenized_sentences_1) == 6 
    return
