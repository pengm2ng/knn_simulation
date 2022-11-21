from resources import knn_function, knn_metric
from matplotlib import pyplot as plt
import numpy as np

candidate = [(2, 3),  (4, 2), (10, 3),  (20, 17),  (13, 10), (30, 12), (20, 12)]
candidate2 = [[2, 3],  [4, 2], [6, 3],  [7, 17],  [13, 10], [30, 12], [20, 12]]
training_points = [(1,1), (10,20) , (40,10), (50,100), (12,10), (14,10)]
training_points2 = [[1,1], [10,10] , [40,10], [50,10], [12,10], [13,10]]
training_labels = [0,0,1,1,2,2]
a= np.array(training_points)
print(a[:,0:1])
b= np.array(candidate)
plt.scatter(a[:,0:1],a[:,1:2])
plt.scatter(b[:,0:1],b[:,1:2])

allocation = knn_function.allocate_frontier_node(2, training_points, training_labels, candidate)

print("할당된 노드: " + str(allocation))
plt.show()