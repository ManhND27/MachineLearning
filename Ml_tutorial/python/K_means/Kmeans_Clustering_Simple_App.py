import numpy as np
from mnist import MNIST
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import normalize

import display_network

from mlxtend.data import loadlocal_mnist
X, y = loadlocal_mnist(images_path='D:/Coder/src/MachineLearning/python/K_means/MNIST/t10k-images.idx3-ubyte',
labels_path='D:/Coder/src/MachineLearning/python/K_means/MNIST/t10k-labels.idx1-ubyte')

X0 = np.asarray(X)[:100,:]/256.0
X = X0

K = 10
kmeans = KMeans(n_clusters=K).fit(X)
pred_label = kmeans.predict(X)

print(type(kmeans.cluster_centers_.T))
print(kmeans.cluster_centers_.T.shape)
A = display_network(kmeans.cluster_centers_.T, K, 1)

print(type(kmeans.cluster_centers_.T))
print(kmeans.cluster_centers_.T.shape)
A = display_network(kmeans.cluster_centers_.T, K, 1)

f1 = plt.imshow(A, interpolation='nearest', cmap = "jet")
f1.axes.get_xaxis().set_visible(False)
f1.axes.get_yaxis().set_visible(False)
plt.show()