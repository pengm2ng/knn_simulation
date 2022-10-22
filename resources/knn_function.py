from sklearn.neighbors import KNeighborsClassifier

def allocate_frontier_node(k_num, training_points, training_labels, pre_frontier_node):
    # 노드를 에이전트 들에게 할당한다.

    classifier = KNeighborsClassifier(n_neighbors=k_num)

    classifier.fit(training_points, training_labels)

    allocation = classifier.predict(pre_frontier_node)

    return allocation