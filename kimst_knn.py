flag = 1


def simulate_kimst_knn(agent_num, map_type, explored_data):
    for monte in range(1, 101):
        print('kimst_knn ' + str(monte))
        for k in range(1, 11):
            cnt = 0
            while flag:
                cnt = cnt + 1

                if flag == 0:
                    break
