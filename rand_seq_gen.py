#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 10:56:28 2017

Script for generating a single random sequence of length 200.
To be run 100 times for the exercise. 

@author: GMA
"""

from numpy import array
# Older version of python on binf server prevents using choices module. 
from numpy.random import choice
from textwrap import fill

SEQ_LENGTH = 200

amino_acids = "ACDEFGHIKLMNPQRSTVWY"
aa_list = list(amino_acids)
frequences = [0.095070, 0.011560, 0.051634, 0.057745, 0.039081, 
              0.073548, 0.022629, 0.060123, 0.043981, 0.106769, 
              0.028008, 0.039309, 0.044342, 0.044409, 0.055342, 
              0.058097, 0.053810, 0.070647, 0.015378, 0.028498]            
# Frequencies (probabilities) have to be normalized for numpy.
frequences = array(frequences)
frequences /= frequences.sum()
              
def make_sequence():
    # Each run will overwrite the file, supplying water with new seq. 
    with open("sequence.fasta","w") as seq:
        seq.write(">SEQ\n")
        seq.write("{}\n".format(fill(''.join(
                    choice(aa_list, SEQ_LENGTH, p=frequences)), 71)))
            
make_sequence()