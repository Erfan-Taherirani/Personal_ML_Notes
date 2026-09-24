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
    - calculate_diversity: Calculates the diversity of an ensemble of models.
    - calculate_prediction_correlations: Calculates the prediction correlations of an ensemble of models.
    - evaluate_model_contributions: Evaluates the contributions of individual models to the ensemble.
    - voting_ensemble_model_contributions: Evaluates the contributions of individual models to the ensemble.
"""
import numpy as np
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier


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


def calculate_diversity(
        predictions_list: list[object],
        X_test: np.ndarray
) -> dict[str, np.ndarray]:
    """ Calculates the diversity of an ensemble of models.

    This function calculates the diversity of an ensemble of models using the disagreement
    between the predictions of the models. It takes a list of models and a test dataset as
    input and returns a dictionary with the diversity and a numpy array of the diversity matrix.
    (Estimators should be fitted before using this function).

    :param predictions_list: List of models.
    :param X_test: Test data.
    :return: Diversity of the ensemble.
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

    return {
        "diversity": diversity_matrix.mean(),
        "diversity_matrix": diversity_matrix
    }


def calculate_prediction_correlations(
        estimators: list[object], X_test: np.ndarray
) -> np.ndarray:
    """
    Calculates the prediction correlations of an ensemble of models.

    This function calculates the prediction correlations of an ensemble of models using the
    Pearson correlation coefficient. It takes a list of models and a test dataset as input and
    returns a numpy array of prediction correlations. (Estimators should be fitted before using
    this function.)
    
    Parameters:
    estimators (list[object]): List of models.
    X_test (numpy array): Test data.
    
    Returns:
    numpy array: Prediction correlations of the ensemble.
    """
    predictions = []
    for estimator in estimators:
        predictions.append(estimator.predict(X_test))

    return np.corrcoef(predictions) # calculate the correlation coefficients between the predictions


def evaluate_model_contributions(
    ensemble: object,
    X: np.ndarray,
    y: np.ndarray
) -> list[float]:
    """ Evaluates the contributions of individual models to the ensemble.

    This function evaluates the contributions of individual models to the ensemble by calculating
    the difference in performance between the ensemble and the ensemble without the current model.
    It takes an ensemble of models, a test dataset, and a target variable as input and returns a
    list of contributions.

    :param ensemble: Ensemble of models.
    :param X: Test data.
    :param y: Target variable.
    :return: List of contributions.
    """
    base_score = ensemble.score(X, y)
    contributions = []
    
    for i, model in enumerate(ensemble.estimators_):
        # Create ensemble without current model
        temp_preds = [est.predict(X) for j, est in enumerate(ensemble.estimators_)
                     if j != i]
        temp_score = accuracy_score(y, np.mean(temp_preds, axis=0) > 0.5)
        
        # Contribution is the difference in performance
        contribution = base_score - temp_score
        contributions.append(contribution)
    
    return contributions


def voting_ensemble_model_contributions(
    ensemble: object,
    X: np.ndarray,
    y: np.ndarray,
    voting: str = "hard"
) -> list[float]:
    """ Evaluates the contributions of individual models to the ensemble.

    This function evaluates the contributions of individual models to the ensemble by calculating
    the difference in performance between the ensemble and the ensemble without the current model.
    It takes an ensemble of models, a test dataset, and a target variable as input and returns a
    list of contributions.

    :param ensemble: Ensemble of models.
    :param X: Test data.
    :param y: Target variable.
    :param voting: Type of voting.
    :return: List of contributions.
    """
    base_score = ensemble.score(X, y)
    contributions = []

    for i, model in enumerate(ensemble.estimators_):
        temp_estimators = [est for j, est in enumerate(ensemble.estimators_) if j != i]
        temp_est = []
        
        for k, model in enumerate(temp_estimators):
            temp_est.append((f"{k}", model))
            
        temp_voting = VotingClassifier(estimators=temp_est, voting=voting)
        score = temp_voting.fit(X, y).score(X, y)
        contribution = base_score - score
        contributions.append(contribution)
        return contributions
