# Use cases for paper-parser package

### Use case #1
User input is a scientific paper on perovskite synthesis (several formats acceptable), and the output is a summary of synthesis steps and parameters, and device performance metrics.

#### Components for use case #1

1. Pre-processing: clean paper and organize into a usable format 
2. Paragraph identification: identify paragraphs of interest and discard all other content. Steps might include subcomponents:
	i. Tokenization: split text into elements
	ii. Tagging: identify relevant entities e.g. precursors, solvents, performance metrics
3. Parsing: scan papers for relevant information and extract,
	i. synthesis steps (as phrases)
	ii. quantitative synthesis parameters (a quantifiable action or specified condition and its related value e.g. temperature of reaction, volume of solvent)
	iii. quantitative device performance/properties (e.g. PCE = 50%)
4. Data visualization: summarize data in a short, understandable format

### Use case #2
User inputs are a few keywords of interest (such as perovskite type, synthesis, and application), which are used to search for relevant papers. The outputs are plots analyzing the relationship between various synthesis parameters and device performance, which are obtained from the library of papers.
(This second use case is the ideal end goal we hope to achieve, but probably too large for the scope of this project.)

#### Components for use case #2
1. User input interface for entering search terms/keywords
2. Search and download papers from online journals in the correct format. Includes accessing online journals and authentication process.
3. Data analytics: Extract relationships from large quantity of synthesis paramters and device performance metrics
