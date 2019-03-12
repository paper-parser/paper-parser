"""
paperparser.parse.order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Searches a given paragraph for synthesis steps and stores steps as an ordered
list.

"""

from chemdataextractor.doc import Paragraph
import nltk

def syn_order(para):
    '''Finds relevant perovskite synthesis steps (using known database) in 
    input paragraph, and returns them in order.
    vb_order is an ordered list of tuples, ordered according to appearance 
    in the paragraph input, with each tuple containing a synthesis step and 
    the sentence number/index it is in. 
    vb_dict is a dict with the keys being sentence number, and values being
    synthesis steps found in that sentence.'''
    
    # Database of relevant perovskite synthesis action words 
    #syn_db = ['deposit', 'pyrolysis', 'spin-coat', 'calcine', 'synthesize',
    #          'react', 'stir', 'evaporate', 'dissolve', 'prepare', 'coat',
    #          'treat', 'drop-cast', 'dry', 'mix', 'anneal']

    syn_db = ['spin-coat', 'coat', 'anneal', 'dry']
    
    vb_order = list()
    vb_dict = {}
    
    for num_s in range(len(para.sentences)):
        vb_arr = list()
        
        # Use NLTK to split sentences into lowercase tokens
        tk = nltk.word_tokenize(str(para[num_s]))
        tk = [w.lower() for w in tk]
        
        # Compares each word in the paragraph to a given database, accounts
        # for verb tenses (past and continuous tense) exceptions
        for word in tk:
            for action in syn_db:
                if ((action[-1] == 'e' or action[-1] == 'y') 
                    and (action[:-1] == word[:len(action)-1])):
                    vb_order.append((action,num_s))
                    vb_arr.append((action))
                elif action == word[:len(action)]:
                    vb_order.append((action,num_s))
                    vb_arr.append((action))
                else:
                    continue
        vb_dict[num_s] = vb_arr
            
    return vb_order, vb_dict