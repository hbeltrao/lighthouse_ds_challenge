"""
This is a boilerplate pipeline 'train_test_split'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import df_splitter


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=df_splitter
            , inputs=['df_with_selected_features', 'params:features', 'params:target']
            , outputs=['train_features', 'test_features', 'train_targets', 'test_targets']
        )
    ])
