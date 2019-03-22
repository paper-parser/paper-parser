


<!-- [![forthebadge](https://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://forthebadge.com) -->

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/paper-parser/paper-parser.svg?branch=master)](https://travis-ci.org/paper-parser/paper-parser)   [![spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)

<p align="center"><img src="https://github.com/paper-parser/paper-parser/blob/master/doc/images/logo.png" width="300" alt="PaperParser"></p>


_WARNING: package is currently in development and not ready for use._


**PaperParser** is a python package for extracting synthesis and performance metrics from academic articles on perovskite solar cells. The long-term goal of this package is to provide a means to (1) scrape, (2) summarize, and (3) compare the relationships between synthesis procedure and device performance across perovskite literature.

# Overview

Each paper is converted into a relational graph like the example below,

<p align="center"><img src="https://github.com/paper-parser/paper-parser/blob/master/doc/images/output_graph.png" width="750" alt="graph"></p>
<!--     Material (some chemical name)
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
    step ordering: ['step 1', 'step 2', 'step 3'] -->

implemented in python as nested dictionaries and lists.

Each paper goes through the following process

![Flowchart for PaperParser workflow](doc/images/pp_flowchart.svg)

# Installation

The simplest way to run the example notebooks is to clone the git repo to your local machine.  To install `paperparser` and it dependencies, we recommend

1. First creating a new conda environment by running the following command in your terminal 
    ```bash
    conda create -n your_new_env python=3.6
    ```
    Since paperparser was designed in python 3.6. 
    <!-- This turns out to be important, because for some reason the verson of pip that comes with the conda installation of python 3.6 does not work with our `setup.py` and `requirements.txt` files. -->

2. Activate your new, clean conda environment
    ```bash
    conda activate your_new_env
    ```

3. A necessary dependency (for Windows computers ?? before the next step)
    ```bash
    conda install -c conda-forge dawg 
    ```
4. pip install in your new conda environment by running 
    ```bash
    pip install .
    ```
    in the top level directory containing `setup.py`. This will automatically install the dependencies required to run the example notebooks. 
5. Get ChemDataExtractor's Data files - a software package that PaperParser is built on, click [here](http://chemdataextractor.org/docs/install) for more installation information
    ```bash
    cde data download
    ```
6. For use of the example notebooks, you will also need jupyter notebooks and pandas, you can install these by the commands
    ```bash
    pip install ipykernel 
    pip install pandas
    ``` 

(from setup.py example [here](https://python-packaging.readthedocs.io/en/latest/minimal.html))


## Dependencies

PaperParser uses the following open-source packages in its implementation:

* [ChemDataExtractor](https://github.com/mcs07/ChemDataExtractor/)
* [spaCy](https://spacy.io)

# User Guide

An example of each tool that makes up `paperparser` is contained within the jupyter notebook `examples/example_notebook.ipynb`. This notebook should not require installation of `paperparser` if run in the original directory structure. 

