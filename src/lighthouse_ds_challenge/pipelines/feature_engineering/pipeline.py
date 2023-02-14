"""
This is a boilerplate pipeline 'feature_engineering'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import select_features, treat_feature_names


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=select_features
            , inputs=["raw_traffic_data", "params:features"]
            , outputs="df_with_selected_features"
        ),
        node(
            func=treat_feature_names
            , inputs=["df_with_selected_features","params:features", "params:target"]
            , outputs=["df_with_treated_selected_features", "treated_features", "treated_target"]
        )
    ])