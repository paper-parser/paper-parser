


<!-- [![forthebadge](https://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://forthebadge.com) -->

[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.org/paper-parser/paper-parser.svg?branch=master)](https://travis-ci.org/paper-parser/paper-parser)   [![spaCy](https://img.shields.io/badge/made%20with%20❤%20and-spaCy-09a3d5.svg)](https://spacy.io)

<p align="center"><img src="https://github.com/paper-parser/paper-parser/blob/master/doc/images/logo.png" width="300" alt="PaperParser"></p>


_WARNING: package is currently in development and not ready for use._


**PaperParser** is a python package for extracting synthesis and performance metrics from academic articles on perovskite solar cells. The long-term goal of this package is to provide a means to (1) scrape, (2) summarize, and (3) compare the relationships between synthesis procedure and device performance across perovskite literature.

# Overview

## How It Works

<p align="center">
![Flowchart for PaperParser workflow](doc/images/pp_flowchart.svg)
</p>

## Output

The result is a relational graph like the example below,

<p align="center"><img src="https://github.com/paper-parser/paper-parser/blob/master/doc/images/output_graph.png" width="600" alt="graph"></p>
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


# Installation

The simplest way to run the example notebooks is to clone the git repo to your local machine.  To install `paperparser` and its dependencies, we recommend the following procedure:

1. Create a new conda environment by running the following command in your terminal.
    ```bash
    conda create -n your_new_env python=3.6
    ```
    (Note: PaperParser was designed in Python 3.6, but also works with 3.5.)
    <!-- This turns out to be important, because for some reason the verson of pip that comes with the conda installation of python 3.6 does not work with our `setup.py` and `requirements.txt` files. -->

2. Activate your new, clean conda environment.
    ```bash
    conda activate your_new_env
    ```

3. (Optional) For users of Git for Windows/Git Bash: run the following command.
    ```bash
    conda install -c conda-forge dawg
    ```
    Note that Linux, Mac, and WSL (Windows Subsystem for Linux) users can skip this step.

4. Navigate to the top-level directory containing `setup.py` and pip install by running
    ```bash
    pip install .
    ```
    This will automatically install the dependencies required to run the package and the provided example notebooks. _Make sure you are in the correct environment before running `pip install`!_

5. Download [ChemDataExtractor](http://chemdataextractor.org/docs/install)'s Data files. This step is important-- PaperParser will not run without this step.
    ```bash
    cde data download
    ```

6. For use of the example notebooks, you will also need jupyter notebooks and pandas, which can be installed using
    ```bash
    pip install ipykernel
    pip install pandas
    ```
<!--(from setup.py example [here](https://python-packaging.readthedocs.io/en/latest/minimal.html))-->

## Dependencies

PaperParser uses the following open-source packages in its implementation:

* [ChemDataExtractor](https://github.com/mcs07/ChemDataExtractor/)
* [spaCy](https://spacy.io)

# User Guide

An example of each tool that makes up `paperparser` is contained within the jupyter notebook `examples/example_notebook.ipynb`. This notebook should not require installation of `paperparser` if run in the original directory structure.

<!--chc: We spend a lot of time talking about how incomplete our package is, so we don't need to get into those details here.

(Another example notebook titled `examples/example_extracted_info.ipynb` contains information on the use of the high-level wrapper to (almost) all of the tools discussed in `examples/example_notebook.ipynb`. This object implements the output graph displayed at the top of this README, albeit in a much more confusing format because we have not yet figured out how to associate each parsed value with a specific chemical name. As of now each value returned from parsing is simply left in order, so that future development to the module `paperparser.extracted_info` could use associations within the respective parsed sentences (as well as between sentences) and eventually return relational data trees like the dream dispayed above.)-->
