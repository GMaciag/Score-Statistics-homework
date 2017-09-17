#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 21:00:50 2017

Script for generating a database of random sequences. 

@author: GMA
"""
# Module choices is only available in python 3.6+.
from random import choices
from textwrap import fill

DB_SIZE = 4183
DB_LENGTH = 319

amino_acids = "ACDEFGHIKLMNPQRSTVWY"
aa_list = list(amino_acids)
frequences = [0.095070, 0.011560, 0.051634, 0.057745, 0.039081, 
              0.073548, 0.022629, 0.060123, 0.043981, 0.106769, 
              0.028008, 0.039309, 0.044342, 0.044409, 0.055342, 
              0.058097, 0.053810, 0.070647, 0.015378, 0.028498]

def make_database():
    with open("database.fasta","w") as db:
        for i in range(DB_SIZE):
            db.write(">DB_{}\n".format(str(i+1)))
            db.write("{}\n".format(fill(''.join(
                    choices(aa_list, frequences, k=DB_LENGTH)), 71)))
            
make_database()