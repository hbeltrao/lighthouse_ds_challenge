"""
This is a boilerplate pipeline 'model_creation_and_training'
generated using Kedro 0.18.4
"""

import pandas as pd
import xgboost as xgb
from sklearn.model_selection import GridSearchCV
import pickle

def param_optimizer(X_train: pd.DataFrame, y_train: pd.DataFrame):
    """
    Simple function to test some parameters and select the best to optimize the model
    """

    regressor = xgb.XGBRegressor(objective='reg:squarederror', seed=123)

    param_grid = {"max_depth": [2, 4, 6]
                  , "n_estimators": [100, 300, 500]
                  , "learning_rate": [0.01, 0.015]
                }
    
    param_search = GridSearchCV(regressor,  param_grid, cv=5).fit(X_train, y_train)

    best_parameters = param_search.best_params_

    return best_parameters

def create_model(best_parameters: dict, X_train: pd.DataFrame, y_train: pd.DataFrame):
    """
    Function that instantiate a XGBoost model using the optimized parameters selected by GridSearchCV
    """
    
    tuned_regressor = xgb.XGBRegressor(learning_rate = best_parameters["learning_rate"]
                                       , n_estimators = best_parameters["n_estimators"]
                                       , max_depth = best_parameters["max_depth"]
                                       , objective='reg:squarederror'
                                       , seed=123
                                    )
    
    fitted_regressor = tuned_regressor.fit(X_train, y_train)

    return fitted_regressor

def test_model(regressor, X_test: pd.DataFrame):

    y_pred = regressor.predict(X_test)

    return y_pred