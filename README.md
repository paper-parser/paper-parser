# Paper-parser

_WARNING: package is currently in development and not ready for use._

A package for extracting synthesis and performance metrics from academic articles on perovskite solar cells. The long-term goal of this package is to provide a means to scrape, summarize, and compare the relationships between synthesis procedure and device performance across perovskite literature.

# Overview

Each paper is converted into a relational graph like the example below

Example graph representation of material object:

    Material (some chemical name)
    |\
    | Performance metrics
    | |\
    | | VOC - # Volts
    | |\
    | | JSC - # Amps
    | |\
    | | PCE - # percent
    | ect
    |
    Synthesis
    |\
    | step 1 - property
    |  \
    |   other property
    |\
    | step 2 - property
    |  \
    |   property
    |\
    | ect. for other steps...
    |
    step ordering: ['step 1', 'step 2', 'step 3']
 
_Here we can insert a flow-chartof how we get from a paper to our end data structure_
<!-- ![Datastructe](https://octodex.github.com/images/yaktocat.png) -->


# Installation

_need to work on this, probably we will just have the user clone the repo and run a python setup script._