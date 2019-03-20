


<!-- [![forthebadge](https://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://forthebadge.com) -->

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/paper-parser/paper-parser.svg?branch=master)](https://travis-ci.org/paper-parser/paper-parser)   [![spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)

<p align="center"><img src="https://github.com/paper-parser/paper-parser/blob/master/doc/images/logo.png" width="300" alt="PaperParser"></p>


_WARNING: package is currently in development and not ready for use._


**PaperParser** is a python package for extracting synthesis and performance metrics from academic articles on perovskite solar cells. The long-term goal of this package is to provide a means to (1) scrape, (2) summarize, and (3) compare the relationships between synthesis procedure and device performance across perovskite literature.

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
    | etc.
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
    | etc. for other steps...
    |
    step ordering: ['step 1', 'step 2', 'step 3']

implemented in python as nested dictionaries and lists.

Each paper goes through the following process

![Flowchart for PaperParser workflow](doc/images/pp_flowchart.svg)

# Installation

Clone the repo to your local machine and then install `paperparser` by

1. First creating a copy on the conda environment `environment.yml` by running 
```bash
conda env create -f environment.yml
```
in your terminal

2. Install the package by running 
```bash
pip install .
```
in the top level directory containing `setup.py`.


## Dependencies

PaperParser uses the following open-source packages in its implementation:

* [ChemDataExtractor](https://github.com/mcs07/ChemDataExtractor/)
* [spaCy](https://spacy.io)

_need to work on this, probably we will just have the user clone the repo and run a python setup script._
