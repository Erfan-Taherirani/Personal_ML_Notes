"""
This module contains utility functions for ensemble methods.

Author: Erfan Taherirani
Date: 2023-03-01
Updated: 2023-03-01
Email: e.taherirani81@gmail.com
Telegram: @www_erfanT_ir

features:
    - WeightedEnsemble: A weighted ensemble of models.
    - calculate_disagreement: Calculates the disagreement between two models.
    - ensemble_diversity_matrix: Calculates the diversity matrix of an ensemble of models.
"""
import numpy as np
from sklearn.model_selection import cross_val_score


# combinig predictions of different models
class WeightedEnsemble:
    def __init__(self: object, models: list[object]) -> None:
        """
        Initializes a weighted ensemble of models.
        
        Parameters:
        models (list[object]): List of models.
        """
        self.models = models
        self.weights = None

    def fit(self: object, X: np.ndarray, y: np.ndarray) -> object:
        """
        Fits the weighted ensemble of models.
        
        Parameters:
        X (numpy array): Training data.
        y (numpy array): Target values.
        
        Returns:
        object: Self.
        """
        scores = []
        for model in self.models:
            cv_score = cross_val_score(model, X, y, cv=5).mean()
            scores.append(cv_score)
            model.fit(X, y) # train the model on whole data

        self.weights = np.array(scores) / np.sum(scores) # normalize the scores 
        return self

    def predict_proba(self: object, X: np.ndarray, n_classes: int = 2) -> np.ndarray:
        """
        Predicts the probabilities of the models in the ensemble.
        
        Parameters:
        X (numpy array): Test data.
        n_classes (int): Number of classes.
        
        Returns:
        numpy array: Probabilities of the models in the ensemble.
        """
        weighted_predictions = np.zeros((X.shape[0], n_classes))
        for weight, model in zip(self.weights, self.models):
            weighted_predictions += weight * model.predict_proba(X) # update the weighted predictions

        return weighted_predictions

    def predict(self: object, X: np.ndarray) -> np.ndarray:
        """
        Predicts the classes of the models in the ensemble.
        
        Parameters:
        X (numpy array): Test data.
        
        Returns:
        numpy array: Classes of the models in the ensemble.
        """
        return np.argmax(self.predict_proba(X), axis=1)


# ensemble model evaluation techniques
def calculate_disagreement(
        model1: object,
        model2: object,
        X_test: np.ndarray
) -> float:
    """
    Calculates the disagreement between two models.
    
    Parameters:
    model1 (object): First model.
    model2 (object): Second model.
    X_test (numpy array): Test data.
    
    Returns:
    float: Disagreement between the two models.
    """
    y_pred1 = model1.predict(X_test) # type: ignore
    y_pred2 = model2.predict(X_test) # type: ignore
    
    disagreement = np.mean(y_pred1 != y_pred2)
    
    return disagreement


def ensemble_diversity_matrix(
        predictions_list: list[object],
        X_test: np.ndarray
) -> np.ndarray:
    """
    Calculates the diversity matrix of an ensemble of models.
    
    Parameters:
    predictions_list (list[object]): List of models.
    
    Returns:
    numpy array: Diversity matrix of the ensemble.
    """
    n_models = len(predictions_list)
    diversity_matrix = np.zeros((n_models, n_models))

    for i in range(n_models):
        for j in range(i+1, n_models):
            div = calculate_disagreement(
                predictions_list[i], predictions_list[j], X_test
            )
            diversity_matrix[i,j] = div
            diversity_matrix[j,i] = div

    return diversity_matrix
