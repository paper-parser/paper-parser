"""
paperparser.parse.order
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Searches a given paragraph for synthesis steps and stores steps as an ordered
list.

"""

## Database containing objects of synthesis steps with associated word
## variants, something like this:

class SynStep(object):

	def __init__(self):
		self.name = 'action'
		self.variants = []

## For example, a SynStep object would have the following attributes
anneal.name = 'anneal'
anneal.variants = ['anneal', 'annealing', 'annealed']

def syn_order(paragraph):
	"""
	Input, paragraph, is a single string of text.

	1) tokenizes the paragraph into words - call something from CDE to do this
	2) compare each token/element to every string in object.variants in 
	SynStep database, and if match is found,
	3) store in an ordered list (df??): Order number/ID, SynStep objection 
	name, Sentence number, (maybe location of word in paragraph since there 
	might be more than one action per sentence. 
	4) Return this list/df
	"""

	return df_syn_order



