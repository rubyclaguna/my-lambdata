import pandas as pd 
import numpy as np 


def datesplit(df, date_column):
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column], infer_datetime_format=True)

    df[date_column+'_YEAR'] = df[date_column].dt.year
    df[date_column+'_MONTH'] = df[date_column].dt.month
    df[date_column+'_DAY'] = df[date_column].dt.day
    return df

