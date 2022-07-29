#Libraries
import numpy as np
import pandas as pd

def formatting (df, *cols):
    '''
    This function takes a dataframe and strips the value of the text columns. 
    
    Parameters
    ----------
    df : dataframe with spaces in the columns
    *cols: column(s) that need to be corrected
    
    Returns
    -------
    df2 : corrected dataframe
    '''
    df2=df
    for col in cols:
        df2=df2.astype({f'{col}': str}, errors='raise')
        df2[f'{col}']=df2[f'{col}'].apply(lambda x: x.strip())
    return df2

def dropping (df, *cols):
    '''
    This function drops column(s) from a dataframe. 
    
    Parameters
    ----------
    df : dataframe with spaces in the columns
    *cols: column(s) that need to be dropped
    
    Returns
    -------
    df2 : corrected dataframe
    '''
    df2=df
    for col in cols:
        df2=df2.drop(columns=f'{col}')
    return df2