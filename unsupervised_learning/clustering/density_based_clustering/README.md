# Density-Based Methods

This type of clustering is based on the idea of grouping data points based on their density. Density-based clustering algorithms are used to identify clusters of data points that are densely packed together.

## Advantages

- Can be used to identify clusters of data points that are densely packed together
- Can be used to identify clusters of data points that are not well separated
- Can capture any arbitrary shape of clusters
- Robust to outliers
- Do not need to specify the number of clusters

## Disadvantages

- Can be computationally expensive for large datasets (medium)
- Need to specify the $\epsilon$ parameter, that is the maximum distance between two data to cluster in the same group
- Need to specify the $\delta$ parameter, that is the minimum number of points required to form a cluster

## Algorithms

- **`DBSCAN`**