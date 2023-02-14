"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from lighthouse_ds_challenge.pipelines import feature_engineering, train_test_split, model_creation_and_training
from lighthouse_ds_challenge.pipelines import api_pipeline


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """

    feature_engineering_pipeline = feature_engineering.create_pipeline()
    train_test_splitter_pipeline = train_test_split.create_pipeline()
    model_creation_and_training_pipeline = model_creation_and_training.create_pipeline()
    api_pipeline_instance = api_pipeline.create_pipeline()

    #pipelines = find_pipelines()
    #pipelines["__default__"] = sum(pipelines.values())
    
    return {
        "feature_engineer" : feature_engineering_pipeline
        , "__default__" : (
            feature_engineering_pipeline
            + train_test_splitter_pipeline
            + model_creation_and_training_pipeline
            + api_pipeline_instance
        )
    }
