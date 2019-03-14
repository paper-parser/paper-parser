"""
paperparser.read_paper.sentence_classifier
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Uses spacy to handle text, and sklearn to build support vector machine model.
Train a predictor model given inputs of a list of sentences, and corresponding
binary tag.
Predict if sentences should be tagged 0 or 1 based on trained model.
"""

# Imports
import extract_sentences
import numpy as np
import pandas as pd
from sklearn.base import TransformerMixin 
from sklearn.feature_extraction.stop_words \
import ENGLISH_STOP_WORDS as stopwords
from sklearn.feature_extraction.text import CountVectorizer 
from sklearn.metrics import accuracy_score 
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from spacy.lang.en import English
import string

# Custom transformer using spaCy 
class predictors(TransformerMixin):
    """
    Class for predictors for model to be built on
    """
    def transform(self, X, **transform_params):
        """Basic text transformation; calls cleaning function"""
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        """Fitting function"""
        return self

    def get_params(self, deep=True):
        """Function to get parameter"""
        return {}


# Basic utility function to clean the text 
def clean_text(text):
    """Cleans text; makes all text lower case"""
    return text.strip().lower()


def spacy_tokenizer(sentence):
    """Create spacy tokenizer that parses a sentence and generates tokens,
    these can also be replaced by word vectors"""
    punctuations = string.punctuation
    parser = English()
    tokens = parser(sentence)
    tokens = [tok.lemma_.lower().strip() 
        if tok.lemma_ != "-PRON-" else tok.lower_ for tok in tokens]
    tokens = [tok for tok in tokens 
        if (tok not in stopwords and tok not in punctuations)]     
    
    return tokens


def train_predictor(X_train, Y_train):
    """Create vectorizer object to generate feature vectors,
    we will use custom spacy’s tokenizer"""
    vectorizer = CountVectorizer(tokenizer = spacy_tokenizer, 
                                ngram_range=(1,1))
    classifier = LinearSVC()

    # Create the  pipeline to clean, tokenize, vectorize, and classify 
    pipe = Pipeline([("cleaner", predictors()),
                     ('vectorizer', vectorizer),
                     ('classifier', classifier)])

    # Fit model using training data
    pipe.fit(X_train, Y_train)

    return pipe


def classify_sentences(model, X_sentences):
    """Uses an input predictor model to classify a list of sentences,
    and returns classified sentences as two separate lists"""
    pred_data = model.predict(X_sentences) 
    predicted_output = pred_data.astype(np.float)
    synthesis_sentence = []
    not_synthesis_sentence = []

    for i in range(len(predicted_output)):
        if predicted_output[i] == 1:
            synthesis_sentence.append(X_sentences[i])
        else:
            not_synthesis_sentence.append(X_sentences[i])
            
    return predicted_output, synthesis_sentence, not_synthesis_sentence