"""
This modules contains the most useful functions and classes needed for the 
ML projects

Author: Erfan Taherirani
Email: e.taherirani81@gmail.com
Github: Erfan-Taherirani
"""
import itertools


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from thefuzz import fuzz
import jellyfish


# __all__=[

# ]


def silhouette_analysis(
        X: np.ndarray, k_range: range, print_scores: bool = False,
        visualization: bool = False, kmeans_params: dict = {}
) -> tuple[int, float]:
    """Calculate the Silhoutte Score to Find the Optimal K

    This function calculates the silhouette score for the k-means clustering
    algorithm and helps you to decide the optimal k value.

    :param X: The input features array
    :param k_range: Range of possible k values
    :param print_scores: If True prints all the scores (k, Silhouette Score),
    defaults to False
    :param visualization: If True visualizes the trend of the Silhouette score
    for different k values, defaults to False
    :param kmeans_params: Custom parameters for the KMeans, defaults to {}
    :return: A tuple of best score (k, Silhouette Score)
    """
    scores = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k, **kmeans_params)
        kmeans.fit(X)
        
        silhouette_score_ = silhouette_score(X, kmeans.labels_)
        scores.append((k, silhouette_score_))
        
    scores = np.array(scores)
    best_score = scores[:, 1].max()
    best_score = scores[scores[:, 1] == best_score]
    
    if print_scores:
        print("Scores:")
        print(scores)
        
    if visualization:
        ax = sns.lineplot(x=scores[:, 0], y=scores[:, 1])
        ax.set_title("Silhouette Score Trend")
        ax.set_ylabel("Silhouette Score")
        ax.set_xlabel("K")
        ax.grid(True, linestyle="--", alpha=0.7)

    print("\nBest Score: (K, Silhouette Score)")
    print(best_score[0])
    return best_score[0]


def elbow_method(X: np.ndarray, k_range: range, kmeans_params: dict = {}) -> None:
    """Visualize the Inertia for the Elbow Method

    :param X: The input features array
    :param k_range: Range of possible k values
    :param kmeans_params: Custom parameters for the KMeans, defaults to {}
    """
    scores = []
    for k in k_range:
        kmeans = KMeans(n_clusters=k, **kmeans_params)
        kmeans.fit(X)
        
        scores.append((k, kmeans.inertia_))

    scores = np.array(scores)
    ax = sns.lineplot(x=scores[:, 0], y=scores[:, 1])
    ax.set_title("Elbow Method Visualization")
    ax.set_xlabel("K")
    ax.set_ylabel("Inertia")
    ax.grid(True, linestyle="--", alpha=0.7)


def gap_statistics():
    pass


def plot_k_distance_graph(X: np.ndarray, n_neighbors: int) -> None:
    """Plot the K-Distance Graph

    Plot the K-Distance Graph used for tuning the epsilon parameter in DBSCAN algorithm.

    :param X: The input array
    :param n_neighbors: Number of neighbors to calculate the distance from
    """
    neigh = NearestNeighbors(n_neighbors=n_neighbors)
    neigh.fit(X)
    distances, _ = neigh.kneighbors(X)
    distances = np.sort(distances[:, n_neighbors - 1])
    
    _, ax = plt.subplots(figsize=(8, 6))
    
    ax.plot(range(len(distances)), distances)
    ax.set_title(f"{n_neighbors}-Distance Graph", fontsize=14, fontweight="bold")
    ax.set_xlabel("Points")
    ax.set_ylabel(f"{n_neighbors}-th Nearest Neighbor Distance")
    ax.grid(True, linestyle="--", alpha=0.7)
    plt.show()


def fuzzy_dedup(
        df: pd.DataFrame,
        feature: str,
        threshold: int = 80,
        scorer = fuzz.ratio
) -> list[tuple]:
    """Calculate the potential duplicates using fuzzy matching techniques.

    :param df: The dataframe
    :param feature: Feature (column) we wanna use in fuzzy matching
    :param threshold: Fuzzy matching score threshold, defaults to 80
    :param scorer: the scorer function from thefuzz.fuzz module, defaults to fuzz.ratio
    :return: A list of tuples with potential duplication possibility.
    """
    potential_duplicates = []
    for (idx1, row1), (idx2, row2) in itertools.combinations(df.iterrows(), 2):
        if scorer(row1[feature], row2[feature]) >= threshold:
            potential_duplicates.append((idx1, idx2))

    print(f"Number of potential duplicates: {len(potential_duplicates)}")
    return potential_duplicates


def phonetic_match(df: pd.DataFrame, feature: str) -> pd.DataFrame:
    """Find phonetic duplicates

    This function creates a new dataframe from the original dataframe with
    another column named 'phonetic' that is sorted based on this new column
    added and helps in identifying phonetic duplicates.

    :param df: The input dataframe.
    :param feature: The column used for phonetic matching.
    :return: New sorted dataframe.
    """
    df['phonetic'] = df[feature].apply(jellyfish.soundex)
    new_df = df[df.duplicated(subset="phonetic", keep=False)].sort_values(by="phonetic")

    print(f"Number of potential duplicates: {df.duplicated(subset="phonetic").sum()}")
    return new_df


# This part is related to the functions that mostly used for feature_selection

# fiter-based methods
def corr_analysis(
        df: pd.DataFrame,
        target_name: str,
        method: str = "pearson",
        threshold: float = 0
) -> pd.DataFrame:
    """Create a data frame of the Correlation analysis

    This function creates a correlation analysis data frame based_on the
    method you choose for the analysis and using threshold argument you can
    filter the results based-on the correlation value. 

    :param df: The input dataframe
    :param target_name: The target variable name
    :param method: The correlation analysis method name, defaults to "pearson"
    :param threshold: Threshold to filter the results, defaults to 0
    :return: The correlation analysis data frame
    """
    try:
        corr = abs(df.drop(target_name, axis=1).corrwith(
            df[target_name], method=method)).sort_values(ascending=False)
        corr_df = pd.DataFrame(corr).rename({0: f"{method}_correlation"}, axis=1)
        
        return corr_df.loc[corr_df[f"{method}_correlation"] > threshold]

    except ValueError:
        print("ValueError: Method argument not exist.")
        print("Methods to choose: ['pearson', 'kendall', 'spearman']")
        return pd.DataFrame()
