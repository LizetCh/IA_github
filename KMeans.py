import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

k_values=[2,3,4,5,6]

# Generate test data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Euclidean distance calculation function (calculates distance between two points)
def euclidean_distance(a, b):
	return np.sqrt(np.sum((a - b) ** 2))
 
# Initialize Centroids Randomly ()
def initialize_centroids(X, k):
    np.random.seed(50)
    random_idx = np.random.permutation(X.shape[0])
    centroids = X[random_idx[:k]]
    return centroids

# Assign clusters
def assign_clusters(X, centroids):
    clusters = []
    for point in X:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        closest_centroid = np.argmin(distances)
        clusters.append(closest_centroid)
    return clusters


# Calculate new centroids – THIS MUST BE COMPLETED BY THE STUDENT
def calculate_new_centroids(X, clusters, k):
    new_centroids = []
    for i in range(k):
        points_in_cluster = X[np.array(clusters) == i]  # Select points of the current cluster
        new_centroid = points_in_cluster.mean(axis=0)  # Calculate the mean of the cluster
        new_centroids.append(new_centroid)
        
    return np.array(new_centroids)

# Calculate the variance
def calculate_variance(X, clusters, centroids):
    variance = 0
    for i, centroid in enumerate(centroids):
        points_in_cluster = X[np.array(clusters) == i]
        variance += np.sum((points_in_cluster - centroid) ** 2)
    return variance
 
# K-Means algorithm – THIS MAY REQUIRE MODIFICATIONS
def k_means(X, k, max_iters=100, tolerance = .000001):
    centroids = initialize_centroids(X, k)
    variances = []

    #implement how to show the initial configuration of datasets and centroids
    # Visualization of initial points
    visualize_initial_configuration(X, centroids)
    
    
    for i in range(max_iters):
        clusters = assign_clusters(X, centroids)
        new_centroids = calculate_new_centroids(X, clusters, k)

        variance = calculate_variance(X, clusters, centroids)
        variances.append(variance)
        # Optional: Implement convergence criteria to stop the algorithm
        # Check for convergence based on change in variance
        if i > 0:  # Skip the first iteration
            variance_change = abs(variances[-2] - variance)
            if variance_change <= tolerance:
                break
            
        centroids = new_centroids

    visualize_clusters(clusters,centroids)
    return variances



def visualize_initial_configuration(X, centroids):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], s=50, c='blue', label='Datos')
    plt.scatter(centroids[:, 0], centroids[:, 1], color='red', s=100, label='Centroides Iniciales')
    plt.title('Initial Configuration of Centroids')
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.legend()
    plt.show()


# Visualization of clusters
def visualize_clusters(clusters,centroids):
  plt.scatter(X[:, 0], X[:, 1], c=clusters, s=50, cmap='viridis')
  plt.scatter([centroid[0] for centroid in centroids], [centroid[1] for centroid in centroids], color='red', s=100, label='Centroids')
  plt.title('Visualization of K-Means Clustering')
  plt.xlabel('X axis')
  plt.ylabel('Y axis')
  plt.legend()

  plt.show()

all_k_variances = []

# Run K-Means
for k in k_values:
    variances = k_means(X,k)
    all_k_variances.append(variances)

# Plotting variances for each K value
plt.figure(figsize=(10, 6))
for idx, k in enumerate(k_values):
    plt.plot(range(1, len(all_k_variances[idx]) + 1), all_k_variances[idx], marker='o', label=f'K = {k}')
plt.title('Change in Variance Through Iterations for Different K Values')
plt.xlabel('Iteration')
plt.ylabel('Variance')
plt.legend(title='Number of Clusters (K)')
plt.grid(True)
plt.show()

k_means(X,4)


