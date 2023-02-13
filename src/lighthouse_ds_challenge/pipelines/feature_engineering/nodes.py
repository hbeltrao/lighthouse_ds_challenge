"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.4
"""

import pandas as pd


def select_features(df: pd.DataFrame, features):
    """
    Function that takes a dataset and a list of features as inputs 
    and return a dataset containing only the selected features
    """

    df_with_selected_features = df[features]

    return df_with_selected_features