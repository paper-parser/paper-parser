from __future__ import absolute_import

import os
from paperparser.read_paper import sentence_classifier
import sklearn
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
import numpy

#with open(os.path.join(os.path.dirname(__file__), '../syn_sen_model.pkl'), 'rb') as syn_pickle:
#    syn_sen_model = joblib.load(syn_pickle) #imported pre-trained model for classfying sentence

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

def test_train_predictor():
    """Test function for training the model"""

    X_train = [
        'We placed approximately 500\u2009mg of CH3NH3I and 100\u2009mg of PbCl2 into separate crucibles.',
        'The device substrates were placed in a substrate holder above the sources with the TiO2-coated FTO side facing down towards the           sources.','1','2']
    Y_train= [1,0,0,1,1]
    try:
        a = sentence_classifier.train_predictor(X_train,Y_train) #will raise an assertion error for length of list
    except (AssertionError):
        pass
    else:
        raise Exception ("Exception not handled by Asserts")

    X_train1= [
        'We placed approximately 500\u2009mg of CH3NH3I and 100\u2009mg of PbCl2 into separate crucibles.',
         'The device substrates were placed in a substrate holder above the sources with the TiO2-coated FTO side facing down towards                the sources.','Once the pressure in the chamber was pumped down to below 10−5\u2009mbar, the two sources were heated                      slightly above their desired deposition temperatures for approximately 5\u2009min (that is, CH3NH3I was heated to about 120                \u2009°C and PbCl2 was heated to about 325\u2009°C) to remove volatile impurities before depositing the materials onto the                substrate.','The substrate holder was rotated to ensure uniform coating throughout deposition, because the right-hand                      source predominantly coats the right-hand side of the substrate and similarly for the left.','The substrate holder was                    water-cooled to approximately 21\u2009°C, though precise measurement of the substrate temperature during deposition was not                performed.']
    Y_train1=['1.0','1.0','1.0','0.0','1.0']
    a1= sentence_classifier.train_predictor(X_train1,Y_train1)
    assert type(a1)==sklearn.pipeline.Pipeline   # output prediction assertion
    return

def test_classify_sentences():
    """Test function for classifying sentences"""

    X_test1= ('abc','cde','efg') #needs a list passed is tuple
    X_test=[
        'A dense blocking layer of TiO2 (bl-TiO2, ∼70 nm in thickness) was deposited onto a F-doped SnO2 (FTO, Pilkington, TEC8) substrate          by spray pyrolysis, using a 20 mM titanium diisopropoxide bis(acetylacetonate) solution (Aldrich) at 450 °C to prevent direct              contact between the FTO and the hole-conducting layer.','A 200–300-nm-thick mesoporous TiO2 (particle size: about 50 nm,                  crystalline phase: anatase) film was spin-coated onto the bl-TiO2/FTO substrate using home-made pastes14 and calcining at 500 °C          for 1 h in air to remove organic components.','CH3NH3I (MAI) and CH3NH3Br (MABr) were first synthesized by reacting 27.86 ml              CH3NH2 (40% in methanol, Junsei Chemical) and 30 ml HI (57 wt% in water, Aldrich) or 44 ml HBr (48 wt% in water, Aldrich) in a            250 ml round-bottom flask at 0 °C for 4 h with stirring, respectively.']


#    try:
#        a = sentence_classifier.classify_sentences(syn_sen_model,X_test1) #will raise an assertion error
#    except (AssertionError):
#        pass
#    else:
#        raise Exception ("Exception not handled by Asserts")

#    pred_data, synthesis_sentences, not_synthesis_sentences = sentence_classifier.classify_sentences(syn_sen_model,X_test)
#    assert type(pred_data)== numpy.ndarray #output check
#    assert type(synthesis_sentences) == type(not_synthesis_sentences) == list #output check
