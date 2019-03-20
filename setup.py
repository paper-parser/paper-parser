#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


if os.path.exists('README.rst'):
    long_description = open('README.rst').read()
else:
    long_description = '''A toolkit for extracting perovskite solar cell synthesis parameters and performance metrics from scientific journals.'''

setup(
    name='PaperParser',
    version='1.0',
    author='Christine Chang, Harrison Goldwyn, Neel Shah, Linnette Teo',
    author_email='changch@uw.edu, goldwyn@uw.edu, neel931@uw.edu, teoqrl@uw.edu',
    license='MIT',
    url='https://github.com/paper-parser/paper-parser',
    packages=find_packages(),
    description='Package to extract perovskite synthesis and performance from literature',
    long_description=long_description,
    keywords='text-mining mining chemistry nlp perovskite synthesis',
    install_requires=[
        'chemdataextractor', 'spacy', 'scikit-learn'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Text Processing :: Markup :: HTML',
    ],
)