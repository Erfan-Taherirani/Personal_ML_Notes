"""
This modules contains the most useful functions and classes needed for the 
ML projects

Author: Erfan Taherirani
Email: e.taherirani81@gmail.com
Github: Erfan-Taherirani
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors


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
