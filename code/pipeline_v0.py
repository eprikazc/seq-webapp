#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 22:16:01 2018

@author: ccchang0111
"""

import pandas as pd
#import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

def seqHeatmap(seq_input):
    """ heatmap of the sequences
    
    Paramters:
    --------
    seq_input: pd.Series
        each serie is a peptide sequence
    """        
    aa_spec = {}
    
    flank_seq_len = len(seq_input.values[0])
    seq2unique = set(seq_input.str.cat())

    for i in range(flank_seq_len):
        aa_count = dict.fromkeys(seq2unique, 0)
        ## count the aa occurance at the selected position(i)
        aa_count.update(Counter(seq_input.str[i])) 
        aa_spec[i] = aa_count
    
    aa_spec = pd.DataFrame(aa_spec) 
    
    # normalize the count to the total sequences
    aa_spec_norm = aa_spec.astype(float)/len(seq_input)
    aa_spec_norm_T = aa_spec_norm.transpose()
    aa_spec_norm_T.reset_index(drop=True, inplace=True) # reset index
    
    aa_spec_plot = sns.heatmap(aa_spec_norm_T.transpose())
    aa_spec_plot.set(xlabel='position', ylabel='characters')
    
    return aa_spec_plot

def pipeline(input_file):
    """perform encoding and then clustering
    
    Parameters:
    --------
    input_file: csv file path
        which contains one column of charaters
        

    Return:
    --------
    df: pd.DataFrame
        a dataframe with additional column of string length 
    df_plot: seaborn plot object
    """
    
    df = pd.read_csv(input_file,
                     header = None, names = ["seqs"])
    df["str_len"] = df.seqs.str.len()
    
    df_plot = seqHeatmap(df.seqs)
    
    return df, df_plot

## example usecase
## out1, out2 = pipeline("input_file.csv")
