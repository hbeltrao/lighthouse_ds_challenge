"""
This is a boilerplate pipeline 'model_creation_and_training'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import create_model, param_optimizer, test_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=param_optimizer
            , inputs=["train_features", "train_targets"]
            , outputs="best_parameters"
        ),
        node(
            func=create_model
            , inputs=["best_parameters", "train_features", "train_targets"]
            , outputs="fitted_regressor"
        ),
        node(
            func=test_model
            , inputs=["fitted_regressor", "test_features"]
            , outputs="model_predictions"
        )
    ])
