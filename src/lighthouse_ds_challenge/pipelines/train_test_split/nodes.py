"""
This is a boilerplate pipeline 'train_test_split'
generated using Kedro 0.18.4
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def df_splitter(df:pd.DataFrame, treated_features, treated_target):
    """
    Basic function to split the dataset into train and test portions,
    saving them into separated  files  to be used
    """
    X = df[treated_features]
    y = df[treated_target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=33)

    return X_train, X_test, y_train, y_test