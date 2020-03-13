#check df for nulls 
import numpy as np
import pandas as pd

def check_nulls(df):
    """
    Function used to check for null values. 
    """
    na_df = df.isna().sum()

    print('Null Values for Features\n')
    print(na_df)

def train_val_test(df):
    """
    Function that train/test/val splits a df
    """
    from sklearn.model_selection import train_test_split
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    train, val = train_test_split(train, test_size=0.25, random_state=42)
    return train.shape, test.shape, val.shape