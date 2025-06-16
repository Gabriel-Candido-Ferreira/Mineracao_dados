from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture

X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=42)

gmm = GaussianMixture(n_components=4, random_state=42)
gmm.fit(X)
labels = gmm.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', marker='o')
plt.title('Clustering com GMM')
plt.xlabel('Primeira variável')
plt.ylabel('Segunda variável')
plt.grid(True)
plt.show()

n_clusters = len(np.unique(labels))
print(f'Número de clusters identificados pelo GMM: {n_clusters}')

means = gmm.means_
covariances = gmm.covariances_

print("Centroides dos clusters:")
print(means)
print("\nMatrizes de covariância:")
print(covariances)
