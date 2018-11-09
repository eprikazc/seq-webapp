#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 22:16:01 2018

@author: ccchang0111
"""

import pandas as pd

def pipeline(input_file, verbose=False):
    """perform encoding and then clustering
    
    Parameters:
    --------
    input_file: csv file path
        which contains one column of charaters
        

    Return:
    --------
    df_out: pd.DataFrame
        a dataframe with additional column of string length 
    """
    
    df = pd.read_csv(input_file,
                     header = None, names = ["seqs"])
    df["str_len"] = df.seqs.str.len()
    
    return df