"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import select_features


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=select_features
            , inputs=["raw_traffic_data", "params:features"]
            , outputs="df_with_selected_features"
        )
    ])