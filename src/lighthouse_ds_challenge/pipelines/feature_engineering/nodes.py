"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.4
"""

import pandas as pd
import re


def select_features(df: pd.DataFrame, features):
    """
    Function that takes a dataset and a list of features as inputs 
    and return a dataset containing only the selected features
    """

    df_with_selected_features = df[features]

    return df_with_selected_features


def treat_feature_names(df: pd.DataFrame, features, target):
    """
    Function to treat feature names to remove spaces and unwanted charachters
    """

    treated_features = []

    treated_target = re.sub(r"[^a-zA-Z0-9 ]", "", target).replace(" ", "_")

    for feature in features:
        treated_feature = re.sub(r"[^a-zA-Z0-9 ]", "", feature).replace(" ", "_")
        treated_features.append(treated_feature)
    
    treated_features_dict = dict(zip(feature, treated_features))

    df_with_treated_selected_features = df.rename(columns=treated_features_dict)

    return df_with_treated_selected_features, treated_features, treated_target

