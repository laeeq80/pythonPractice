import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


# Step 1: Create a dataset
def create_dataset():
    # Generate synthetic data with 300 samples, 2 features (age, spending score), and 4 centers (clusters)
    X, y = make_blobs(n_samples=300, centers=4, cluster_std=1.0, random_state=42)
    dataset = pd.DataFrame(X, columns=["Feature1", "Feature2"])
    return dataset


# Step 2: Apply K-Means Clustering
def apply_kmeans(dataset, n_clusters=4):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    dataset['Cluster'] = kmeans.fit_predict(dataset)
    return kmeans, dataset


# Step 3: Visualize the Clusters
def visualize_clusters(dataset, kmeans):
    plt.figure(figsize=(8, 6))

    # Plot each cluster
    for cluster_id in range(kmeans.n_clusters):
        cluster_data = dataset[dataset['Cluster'] == cluster_id]
        plt.scatter(cluster_data['Feature1'], cluster_data['Feature2'], label=f"Cluster {cluster_id}")

    # Plot cluster centers
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1],
                s=200, c='red', label='Centroids', marker='X')

    plt.title("K-Means Clustering Visualization")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.grid(True)
    plt.show()


# Main execution
if __name__ == "__main__":
    dataset = create_dataset()  # Step 1: Create dataset
    kmeans, clustered_data = apply_kmeans(dataset, n_clusters=4)  # Step 2: Apply K-Means
    visualize_clusters(clustered_data, kmeans)  # Step 3: Visualize clusters
