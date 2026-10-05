# Hierarchical Methods

This type of clustering is based on the idea of creating a hierarchy of clusters. There are two main hierarchical methods:

- **Agglomerative**
    - Start with each data point as a separate cluster
    - Merge the closest pair of clusters until there is only one cluster
    - Repeat the process until all data points are in a single cluster
- **Divisive**
    - Start with all data points in a single cluster
    - Split the cluster into two or more clusters until there is only one cluster
    - Repeat the process until all data points are in a single cluster

> **Note:** Agglomerative clustering is a bottom-up approach, while divisive clustering is a top-down approach.

## Advantages

- Gives hierarchical structure to the clusters

## Disadvantages

- Can be computationally expensive for large datasets
- Can be sensitive to outliers (medium)

## Algorithms

- **Agglomerative Clustering**
    - **`HDBSCAN`**

- **Divisive Clustering**
