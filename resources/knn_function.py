from sklearn.neighbors import KNeighborsClassifier
from matplotlib import pyplot as plt
from matplotlib import colors
from resources import knn_metric
def allocate_frontier_node(k_num, training_points, training_labels, pre_frontier_node):
    # 노드를 에이전트 들에게 할당한다.

    classifier = KNeighborsClassifier(n_neighbors=k_num , metric = 'euclidean')
    print(classifier)
    classifier.fit(training_points, training_labels)

    allocation = classifier.predict(pre_frontier_node)

    return allocation
def allocate_frontier_node2(k_num, training_points, training_labels, pre_frontier_node):
    # 노드를 에이전트 들에게 할당한다.

    classifier = KNeighborsClassifier(n_neighbors=k_num)
    print(classifier)
    classifier.fit(training_points, training_labels)

    allocation = classifier.predict(pre_frontier_node)

    return allocation

def show_plt(candidate_node_list, allocation, training_points, training_labels ,map_type, map_size):

    '''

    :param candidate_node_list: allocation에 맞춰서 training points를 agent+10만큼 표시
    :param allocation:
    :param training_points: 라벨에 맞춰서 training points를 지도에다가 agent+3만큼 표시
    :param training_labels:
    :param map_type:
    :param map_size:
    :return:
    '''

    for i,v in enumerate(candidate_node_list):
        map_type[v[0]][v[1]] = allocation[i]+10


    for i,v in enumerate(training_points):
        map_type[v[0]][v[1]] = allocation[i]+3


    cmap = colors.ListedColormap(['white', 'blue', 'red', 'salmon', 'green', 'black', 'purple', 'orange','lime','cyan','pink','indigo','lavender', 'crimson'])
    plt.figure(figsize=(6, 6))
    plt.pcolor(map_type[::-1], cmap=cmap, edgecolors='k', linewidths=3)
    plt.axis('off')
    plt.show()