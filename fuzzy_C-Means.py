import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import skfuzzy as fuzz

data = pd.read_csv("Pengunjung_mall.csv")
features = data[['Usia', 'Pendapatan (juta Rp)']]

# Number of clusters
n_clusters = int(input("Masukan Jumlah Cluster : "))

# Fuzzy c-means algorithm
cntr, u, u0, d, jm, p, fpc = fuzz.cluster.cmeans(features.T, n_clusters, 2, error=0.005, maxiter=1000)

# Assign each data point to the cluster with the highest membership value
cluster_membership = np.argmax(u, axis=0)

# Plotting the results
fig, ax = plt.subplots()
colors = ['g', 'b', 'c', 'm', 'y', 'k']
for j in range(n_clusters):
    ax.scatter(data[cluster_membership == j]['Usia'], data[cluster_membership == j]['Pendapatan (juta Rp)'],
               c=colors[j], label=f'Cluster {j + 1}', marker='o')
    
# Plot centroids
for i in range(n_clusters):
    ax.scatter(cntr[i, 0], cntr[i, 1], marker='o', s=20, linewidths=3, color='red', label=f'Centroid {i + 1}')

ax.legend()
plt.xlabel('Usia')
plt.ylabel('Pendapatan (juta Rp)')
plt.title('Fuzzy C-Means Clustering')
plt.show()


