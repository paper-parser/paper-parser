<!-- .. image:: https://img.shields.io/badge/license-MIT-green.svg
   :target: https://github.com/paper-parser/paper-parser/blob/master/LICENSE
   :alt: MIT License badge
 -->
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)



# Paper-parser

_WARNING: package is currently in development and not ready for use._

A python package for extracting synthesis and performance metrics from academic articles on perovskite solar cells. The long-term goal of this package is to provide a means to 1) scrape, 2) summarize, and 3) compare the relationships between synthesis procedure and device performance across perovskite literature.

# Overview

Each paper is converted into a relational graph like the example below,

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

implemented in python as nested dictionaries and lists. 

Each paper goes through the following process 

(_insert flow chart here_)

# Installation

_need to work on this, probably we will just have the user clone the repo and run a python setup script._