from sklearn.neighbors import KNeighborsClassifier

def allocate_frontier_node(cnt, agent_num, k , training_points, training_labels, pre_frontier_node):
    # 노드를 에이전트 들에게 할당한다.
    if cnt == 0:
        classifier = KNeighborsClassifier(n_neighbors=3)
    else:
        classifier = KNeighborsClassifier(n_neighbors=5)

    classifier.fit(training_points, training_labels)

    allocation = classifier.predict(pre_frontier_node)
    print("knn으로 할당된 node의 agent: " + str(allocation))

    return allocation