from matplotlib import pyplot as plt
from matplotlib import colors
from resources.agent import Agent
from sklearn.neighbors import KNeighborsClassifier
import math
import random
from resources.map import map_data3


# 갈 수 있는 frontier_node를 모두 찾아서 저장해서 출력한다.
# for문을 일일히 다 돌림.
# 해당하는 부분이 3인 부분인데, 8방위 중에 0이 존재하는 경우 뽑아내서 변수에 저장
def find_frontier_node():
    sum = 0
    for i in range(1, 19):
        for j in range(1, 19):
            sum = sum + 1
            if explored_data[i][j] == 3:
                if explored_data[i][j - 1] == 0 or explored_data[i][j + 1] == 0 or explored_data[i + 1][j] == 0 or \
                        explored_data[i - 1][j] == 0 or explored_data[i - 1][j - 1] == 0 or explored_data[i + 1][
                    j - 1] == 0 or explored_data[i + 1][j + 1] == 0 or explored_data[i - 1][j + 1] == 0:
                    pre_frontier_node.append([i, j])



def set_explored_map(position):
    explored_data[position.x][position.y] = 1

    # 8방위 모두 가능한 경우
    if 1 <= position.x <= 18 and 1 <= position.y <= 18:
        # 오른쪽
        if explored_data[position.x + 1][position.y] == 0:
            if map_data[position.x + 1][position.y] == 0:
                explored_data[position.x + 1][position.y] = 3
            else:
                explored_data[position.x + 1][position.y] = 4
        # 왼쪽
        if explored_data[position.x - 1][position.y] == 0:
            if map_data[position.x - 1][position.y] == 0:
                explored_data[position.x - 1][position.y] = 3
            else:
                explored_data[position.x - 1][position.y] = 4
        # 아래쪽
        if explored_data[position.x][position.y - 1] == 0:
            if map_data[position.x][position.y - 1] == 0:
                explored_data[position.x][position.y - 1] = 3
            else:
                explored_data[position.x][position.y - 1] = 4
        # 위쪽
        if explored_data[position.x][position.y + 1] == 0:
            if map_data[position.x][position.y + 1] == 0:
                explored_data[position.x][position.y + 1] = 3
            else:
                explored_data[position.x][position.y + 1] = 4
        # 오른 위
        if explored_data[position.x + 1][position.y + 1] == 0:
            if map_data[position.x + 1][position.y + 1] == 0:
                explored_data[position.x + 1][position.y + 1] = 3
            else:
                explored_data[position.x + 1][position.y + 1] = 4
        # 오른 아래
        if explored_data[position.x + 1][position.y - 1] == 0:
            if map_data[position.x + 1][position.y - 1] == 0:
                explored_data[position.x + 1][position.y - 1] = 3
            else:
                explored_data[position.x + 1][position.y - 1] = 4
        # 왼 위
        if explored_data[position.x - 1][position.y + 1] == 0:
            if map_data[position.x - 1][position.y + 1] == 0:
                explored_data[position.x - 1][position.y + 1] = 3
            else:
                explored_data[position.x - 1][position.y + 1] = 4
        # 왼 아래
        if explored_data[position.x - 1][position.y - 1] == 0:
            if map_data[position.x - 1][position.y - 1] == 0:
                explored_data[position.x - 1][position.y - 1] = 3
            else:
                explored_data[position.x - 1][position.y - 1] = 4


def set_explored_passnode(position):
    explored_data[position.x][position.y] = 2


def distance(x1, y1, x2, y2):
    result = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    return result

knn_monte_passnode =0
knn_monte_iter = 0
frontier_monte_passnode = 0
frontier_monte_iter = 0
n= 7
knn_monte_coverage = [0 for i in range(100)]
frontier_monte_coverage = [0 for i in range(100)]

for monte in range(n):

    # map_data 0~19까지 indexing 가능하지만, 좌표는 반대로 적용됨.
    # map data는 단지 map을 확인하고 explored_data를 갱신하기 위한 대조용 map
    map_data = map_data3

    # explored_data는 현재 로봇의 위치와 현재까지 탐사된 지역의 특징을 표현한 map
    #     - close =4
    #     - 센서로 탐사된 곳 open = 3
    #     - passnode = 2
    #     - agent의 위치 = 1
    #     - 미탐사 구역 = 0

    explored_data = [
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],

    ]

    # 예비 frontier node

    agent1_x=0
    agent1_y=0
    agent2_x=0
    agent2_y=0
    agent3_x=0
    agent4_x=0
    list = []
    ran_num = random.randint(1,19)

    for i in range(3):
        while ran_num in list:
            ran_num = random.randint(1,19)
        list.append(ran_num)

    agent1_x = list[0]
    agent2_x = list[1]
    agent3_x = list[2]

    list = []
    for i in range(3):
        while ran_num in list:
            ran_num = random.randint(1,19)
        list.append(ran_num)

    agent1_y = list[0]
    agent2_y = list[1]
    agent3_y = list[2]


    time = 0
    iter_max = 0
    result = 0
    coverage_data = []
    iter_data = []
    knn_passnode = 0
    knn_iter_count=0
    frontier_iter_count=0
    coverage10=0
    coverage20=0
    coverage30=0
    coverage40=0
    coverage50=0
    coverage=0


    ## agent start
    agent1 = Agent(agent1_x, agent1_y, [])
    agent2 = Agent(agent2_x, agent2_y, [])
    agent3 = Agent(agent3_x, agent3_y, [])

    ## for loop
    for i in range(100):
        if coverage >0.95:
            knn_iter_count = i
            break
        pre_frontier_node = []
        print("***************iter = " + str(i) + "***************")

        # sensor를 통해서 8방위 explored map 갱신
        # 해당 좌표를 map_data에서 뽑아와서 아래와 같이 바꾼다.
        #     - close =4
        #     - 센서로 탐사된 곳 open = 3
        #     - passnode= 2
        #     - agent의 위치 = 1
        #     - 미탐사 구역 = 0
        print("***************현재 위치에서 map 탐사하기***************")
        set_explored_map(agent1.get_position())
        set_explored_map(agent2.get_position())
        set_explored_map(agent3.get_position())

        if i == 0 or i == 10 or i == 20 or i == 30 or i == 40 or i == 50:
            explored_data[18][1] = 5
            explored_data[18][2] = 5
            explored_data[18][3] = 5
            # cmap = colors.ListedColormap(['white', 'red', 'green', 'blue', 'black', 'yellow'])
            # plt.figure(figsize=(6, 6))
            # plt.pcolor(explored_data[::-1], cmap=cmap, edgecolors='k', linewidths=3)
            # plt.axis('off')

        print("***************다음 frontier node 검색****************")
        # 다음 frontier node를 찾는다.
        # 각 agent에 대한 frontier node 발생
        # 현재 agent 들이 갈 수 있는 모든 frontier node를 저장
        # knn을 통해서 저장된 frontier node의 속성 값 부여 k=????
        # 그중에서 가장 가까운 frontier node로 이동
        # 각각의 agent에 대하여 미탐사 구역을 knn 돌려서 k=1일때 하나 찾아서 가장가까운 곳으로 이동??
        # -> 문제점 - 중간에 장애물이 있을 경우 문제 발생
        find_frontier_node()
        print(pre_frontier_node)

        # agent의 passnode를 갱신한다.
        agent1.set_passnode()
        agent2.set_passnode()
        agent3.set_passnode()

        print("***************knn을 통해서 모든 node 분류**************")
        training_points = agent1.get_passnode().passnode + agent2.get_passnode().passnode + agent3.get_passnode().passnode
        training_labels = []

        for i1 in agent1.get_passnode().passnode:
            training_labels.append(1)
        for i2 in agent2.get_passnode().passnode:
            training_labels.append(2)
        for i3 in agent3.get_passnode().passnode:
            training_labels.append(3)

        print("training point: " + str(training_points))
        print("training label: " + str(training_labels))
        if i == 0:
            classifier = KNeighborsClassifier(n_neighbors=3)
        else:
            classifier = KNeighborsClassifier(n_neighbors=5)

        classifier.fit(training_points, training_labels)

        allocation = classifier.predict(pre_frontier_node)
        print("knn으로 할당된 node의 agent: " + str(allocation))

        print("***************거리 짧은 것 선택************************")
        # passnode를 통해서 knn을 통해 가장 경향성이 비슷하고 거리적으로 가까운 지점 결정
        max1 = 999
        max2 = 999
        max3 = 999
        selected_node1 = 9999
        selected_node2 = 9999
        selected_node3 = 9999

        for iter, val in enumerate(allocation):
            print(val)
            if val == 1:
                temp1 = distance(agent1.get_position().x, agent1.get_position().y, pre_frontier_node[iter][0],
                                 pre_frontier_node[iter][1])
                if temp1 <= max1:
                    max1 = temp1
                    next_x1 = pre_frontier_node[iter][0]
                    next_y1 = pre_frontier_node[iter][1]
                    selected_node1 = iter
            if val == 2:
                temp2 = distance(agent2.get_position().x, agent2.get_position().y, pre_frontier_node[iter][0],
                                 pre_frontier_node[iter][1])
                if temp2 <= max2:
                    max2 = temp2
                    next_x2 = pre_frontier_node[iter][0]
                    next_y2 = pre_frontier_node[iter][1]
                    selected_node2 = iter
            if val == 3:
                temp3 = distance(agent3.get_position().x, agent3.get_position().y, pre_frontier_node[iter][0],
                                 pre_frontier_node[iter][1])
                if temp3 <= max3:
                    max3 = temp3
                    next_x3 = pre_frontier_node[iter][0]
                    next_y3 = pre_frontier_node[iter][1]
                    selected_node3 = iter

        print("*******************************1차 선택된 node*********************************************")
        print(selected_node1)
        print(selected_node2)
        print(selected_node3)
        print("*******************************1차 선택된 node*********************************************")
        node_length = len(pre_frontier_node)

        pop_num = 0
        pop_flag1 = 0
        pop_flag2 = 0
        pop_flag3 = 0

        if selected_node1 != 9999:
            pop_num = pop_num + 1
            pop_flag1 = 1
            pop1 = pre_frontier_node[selected_node1]
        if selected_node2 != 9999:
            pop_num = pop_num + 1
            pop_flag2 = 1
            pop2 = pre_frontier_node[selected_node2]

        if selected_node3 != 9999:
            pop_num = pop_num + 1
            pop_flag3 = 1
            pop3 = pre_frontier_node[selected_node3]

        if pop_flag1:
            pre_frontier_node.remove(pop1)
        if pop_flag2:
            pre_frontier_node.remove(pop2)
        if pop_flag3:
            pre_frontier_node.remove(pop3)

        # node_length와 pop된 pre_frontier_node의 길이를 빼서 개수대로 if문 만들기
        pop_differ = node_length - pop_num

        node_num1 = []
        node_num2 = []
        node_num3 = []

        # pop_differ가 1 -> 하나도 선택된게 없는 경우가 2개.
        # pop_differ가 2 -> 하나도 선택된게 없는 경우가 1개.
        for iter, val in enumerate(pre_frontier_node):
            temp1 = distance(agent1.get_position().x, agent1.get_position().y, pre_frontier_node[iter][0],
                             pre_frontier_node[iter][1])
            node_num1.append([temp1, iter])

            temp2 = distance(agent2.get_position().x, agent2.get_position().y, pre_frontier_node[iter][0],
                             pre_frontier_node[iter][1])
            node_num2.append([temp2, iter])

            temp3 = distance(agent3.get_position().x, agent3.get_position().y, pre_frontier_node[iter][0],
                             pre_frontier_node[iter][1])
            node_num3.append([temp3, iter])

        print(node_num1)
        print(node_num2)
        print(node_num3)

        if pop_num == 1:
            # 1,2가 선택되지 않는 경우
            if selected_node1 == 9999 and selected_node2 == 9999:
                print("agent1, agent2가 선택되지 않음.")
                for iter1, val1 in enumerate(node_num1):
                    for iter2, val2 in enumerate(node_num2):
                        if iter1 == iter2:
                            continue
                        else:
                            total = node_num1[iter1][1] + node_num2[iter2][1]
                            flag1 = iter1
                            flag2 = iter2

                            a = pre_frontier_node[flag1]
                            b = pre_frontier_node[flag2]
                            next_x1 = a[0]
                            next_y1 = a[1]
                            next_x2 = b[0]
                            next_y2 = b[1]

            # 1,3이 선택되지 않는 경우
            if selected_node1 == 9999 and selected_node3 == 9999:
                print("agent1, agent3가 선택되지 않음.")
                for iter1, val1 in enumerate(node_num1):
                    for iter3, val3 in enumerate(node_num3):
                        if iter1 == iter3:
                            continue
                        else:
                            total = node_num1[iter1][1] + node_num3[iter3][1]
                            flag1 = iter1
                            flag3 = iter3
                            a = pre_frontier_node[flag1]
                            c = pre_frontier_node[flag3]
                            next_x1 = a[0]
                            next_y1 = a[1]
                            next_x3 = c[0]
                            next_y3 = c[1]

            # 2,3이 선택되지 않는 경우
            if selected_node2 == 9999 and selected_node3 == 9999:
                print("agent2, agent3가 선택되지 않음.")
                for iter2, val2 in enumerate(node_num2):
                    for iter3, val3 in enumerate(node_num3):
                        if iter2 == iter3:
                            continue
                        else:
                            total = node_num2[iter2][1] + node_num3[iter3][1]
                            flag2 = iter2
                            flag3 = iter3
                            b = pre_frontier_node[flag2]
                            c = pre_frontier_node[flag3]
                            next_x2 = b[0]
                            next_y2 = b[1]
                            next_x3 = c[0]
                            next_y3 = c[1]

        elif pop_num == 2:
            # 1이 선택되지 않는 경우
            if selected_node1 == 9999:
                print("agent1가 선택되지 않음.")
                node_num1.sort()
                print(node_num1)
                next_x1 = pre_frontier_node[node_num1[0][1]][0]
                next_y1 = pre_frontier_node[node_num1[0][1]][1]
                print(pre_frontier_node[node_num1[0][1]][0], pre_frontier_node[node_num1[0][1]][1])
            # 2가 선택되지 않는 경우
            if selected_node2 == 9999:
                print("agent2가 선택되지 않음.")
                node_num2.sort()
                print(node_num2)
                next_x2 = pre_frontier_node[node_num2[0][1]][0]
                next_y2 = pre_frontier_node[node_num2[0][1]][1]
                print(pre_frontier_node[node_num2[0][1]][0], pre_frontier_node[node_num2[0][1]][1])

            # 3이 선택되지 않는 경우우
            if selected_node3 == 9999:
                print("agent3가 선택되지 않음.")
                node_num3.sort()
                print(node_num3)
                next_x3 = pre_frontier_node[node_num3[0][1]][0]
                next_y3 = pre_frontier_node[node_num3[0][1]][1]
                print(pre_frontier_node[node_num3[0][1]][0], pre_frontier_node[node_num3[0][1]][1])

        print(str(next_x1) + " " + str(next_y1))
        print(str(next_x2) + " " + str(next_y2))
        print(str(next_x3) + " " + str(next_y3))

        print("**********************이동****************************\n\n\n")
        # agent가 있던 자리를 node로 저장한다.
        set_explored_passnode(agent1.get_position())
        set_explored_passnode(agent2.get_position())
        set_explored_passnode(agent3.get_position())

        # agent를 이동시킨다.
        agent1.set_position(next_x1, next_y1)
        agent2.set_position(next_x2, next_y2)
        agent3.set_position(next_x3, next_y3)

        if i == 10:

            sum10 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum10 = sum10 + 1

            coverage10 = (324 - sum10) / 324

        if i == 20:

            sum20 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum20 = sum20 + 1

            coverage20 = (324 - sum20) / 324

        if i == 30:

            sum30 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum30 = sum30 + 1

            coverage30 = (324 - sum30) / 324
        if i == 40:

            sum40 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum40 = sum40 + 1

            coverage40 = (324 - sum40) / 324

        if i == 50:

            sum50 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum50 = sum50 + 1

            coverage50 = (324 - sum50) / 324

        sum = 0
        for j in range(1, 19):
            for k in range(1, 19):
                if explored_data[j][k] == 0:
                    sum = sum + 1
        coverage = (324 - sum) / 324




        knn_monte_coverage[i] = knn_monte_coverage[i] + coverage
        iter_data.append(i)

        # agent와 다음 frontier node의 이동거리 계산
        # 이동거리 만큼 +1 -> 계산값이 가장 큰값을 time 변수에 추가
    knn_data = [coverage10, coverage20, coverage30, coverage40, coverage50]

    knn_pass_node = 0
    for i in range(1, 19):
        for j in range(1, 19):
            if explored_data[i][j] == 2:
                knn_pass_node = knn_pass_node + 1

    coverage_pass = knn_pass_node / 324

    # for j in range(1, 19):
    #     for k in range((1, 19)):
    #         if explored_data[j][k] == 2:
    #             knn_passnode = knn_passnode + 1

    print("*******************************제안기법 결과*************************************")
    print("총 탐사율 10iter: " + str(coverage10))
    print("총 탐사율 50iter: " + str(coverage50))
    print("총 탐사율 " + str(result) + "iter: " + str(coverage))
    print("지나간 노드 개수: " + str(coverage_pass))
    #plt.plot(iter_data, coverage_data, 'b--')

    explored_data = [
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4],
        [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],

    ]

    # 예비 frontier node

    time = 0
    iter_max = 0
    coverage_data = []
    iter_data = []
    frontier_passnode = 0
    coverage= 0

    ## agent start
    agent1 = Agent(18, 1, [])
    agent2 = Agent(18, 2, [])
    agent3 = Agent(18, 3, [])

    ## for loop
    for i in range(100):
        if coverage >0.95:
            frontier_iter_count = i
            break
        pre_frontier_node = []
        print("***************iter = " + str(i) + "***************")

        # sensor를 통해서 8방위 explored map 갱신
        # 해당 좌표를 map_data에서 뽑아와서 아래와 같이 바꾼다.
        #     - close =4
        #     - 센서로 탐사된 곳 open = 3
        #     - passnode= 2
        #     - agent의 위치 = 1
        #     - 미탐사 구역 = 0
        print("***************현재 위치에서 map 탐사하기***************")
        set_explored_map(agent1.get_position())
        set_explored_map(agent2.get_position())
        set_explored_map(agent3.get_position())

        print("***************다음 frontier node 검색****************")
        # 다음 frontier node를 찾는다.
        # 각 agent에 대한 frontier node 발생
        # 현재 agent 들이 갈 수 있는 모든 frontier node를 저장
        # knn을 통해서 저장된 frontier node의 속성 값 부여 k=????
        # 그중에서 가장 가까운 frontier node로 이동
        # 각각의 agent에 대하여 미탐사 구역을 knn 돌려서 k=1일때 하나 찾아서 가장가까운 곳으로 이동??
        # -> 문제점 - 중간에 장애물이 있을 경우 문제 발생
        find_frontier_node()
        print(pre_frontier_node)

        # agent의 passnode를 갱신한다.
        agent1.set_passnode()
        agent2.set_passnode()
        agent3.set_passnode()

        print("***************거리 짧은 것 선택************************")
        # passnode를 통해서 knn을 통해 가장 경향성이 비슷하고 거리적으로 가까운 지점 결정
        max1x = 0
        max1y = 0
        max2x = 0
        max2y = 0
        max3x = 0
        max3y = 0
        max1 = 999
        max2 = 999
        max3 = 999

        # 모든 pre_frontier_node 와 모든 agent 사이의 거리를 계산하여 거리가 짧은 걸로 할당
        # agent1이랑 모든 frontier_node 거리구하기
        # agent2랑 모든 frontier_node 거리 구하기
        # agent3랑 모든 frontier_node 거리 구하기
        # agent1 가장짧은 node, agent2 가장 짧은 node, agent3 가장 짧은 node 선택
        # 만약 같은 노드라면 agent끼리의 거리가 더 작은 것을 선택 , 밀려난 agent는 다음 node 선택
        node_num1 = []
        node_num2 = []
        node_num3 = []
        for iter, val in enumerate(pre_frontier_node):
            temp1 = distance(agent1.get_position().x, agent1.get_position().y, pre_frontier_node[iter][0],
                             pre_frontier_node[iter][1])
            node_num1.append([iter, temp1])

            temp2 = distance(agent2.get_position().x, agent2.get_position().y, pre_frontier_node[iter][0],
                             pre_frontier_node[iter][1])
            node_num2.append([iter, temp2])

            temp3 = distance(agent3.get_position().x, agent3.get_position().y, pre_frontier_node[iter][0],
                             pre_frontier_node[iter][1])
            node_num3.append([iter, temp3])

        print(node_num1)
        print(node_num2)
        print(node_num3)

        total_length_list = []

        for iter1, val1 in enumerate(node_num1):
            for iter2, val2 in enumerate(node_num2):
                if iter1 == iter2:
                    continue
                else:
                    total = node_num1[iter1][1] + node_num2[iter2][1]
                    flag1 = iter1
                    flag2 = iter2

                    for iter3, val3 in enumerate(node_num3):
                        if iter2 == iter3 or iter1 == iter3:
                            continue
                        else:
                            total = total + node_num3[iter3][1]
                            flag3 = iter3
                            total_length_list.append([total, flag1, flag2, flag3])

        total_length_list.sort()
        print(total_length_list)

        a = pre_frontier_node[total_length_list[0][1]]
        b = pre_frontier_node[total_length_list[0][2]]
        c = pre_frontier_node[total_length_list[0][3]]
        print(a)
        print(b)
        print(c)

        next_x1 = a[0]
        next_y1 = a[1]
        next_x2 = b[0]
        next_y2 = b[1]
        next_x3 = c[0]
        next_y3 = c[1]

        print(str(next_x1) + " " + str(next_y1))
        print(str(next_x2) + " " + str(next_y2))
        print(str(next_x3) + " " + str(next_y3))

        print("**********************이동****************************")
        # agent가 있던 자리를 node로 저장한다.
        set_explored_passnode(agent1.get_position())
        set_explored_passnode(agent2.get_position())
        set_explored_passnode(agent3.get_position())

        # agent를 이동시킨다.
        agent1.set_position(next_x1, next_y1)
        agent2.set_position(next_x2, next_y2)
        agent3.set_position(next_x3, next_y3)

        if i == 10:

            sum10 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum10 = sum10 + 1

            coverage10 = (324 - sum10) / 324

        if i == 20:

            sum20 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum20 = sum20 + 1

            coverage20 = (324 - sum20) / 324

        if i == 30:

            sum30 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum30 = sum30 + 1

            coverage30 = (324 - sum30) / 324
        if i == 40:

            sum40 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum40 = sum40 + 1

            coverage40 = (324 - sum40) / 324

        if i == 50:

            sum50 = 0
            for j in range(1, 19):
                for k in range(1, 19):
                    if explored_data[j][k] == 0:
                        sum50 = sum50 + 1

            coverage50 = (324 - sum50) / 324

        sum = 0
        for j in range(1, 19):
            for k in range(1, 19):
                if explored_data[j][k] == 0:
                    sum = sum + 1
        coverage = (324 - sum) / 324

        frontier_monte_coverage[i] = frontier_monte_coverage[i] + coverage
        iter_data.append(i)



        # agent와 다음 frontier node의 이동거리 계산
        # 이동거리 만큼 +1 -> 계산값이 가장 큰값을 time 변수에 추가

    frontier_data = [coverage10, coverage20, coverage30, coverage40, coverage50]

    sum100 = 0
    for i in range(1, 19):
        for j in range(1, 19):
            if explored_data[i][j] == 0:
                sum100 = sum100 + 1

    coverage100 = (324 - sum100) / 324

    frontier_pass_node = 0
    for i in range(1, 19):
        for j in range(1, 19):
            if explored_data[i][j] == 2:
                frontier_pass_node = frontier_pass_node + 1

    coverage_pass = frontier_pass_node / 324

    # for i in range(1, 19):
    #     for j in range((1, 19)):
    #         if explored_data[i][j] == 2:
    #             frontier_passnode = frontier_passnode + 1
    print("\n\n\n\n*******************************제안기법 결과*************************************")
    # print("총 탐사율 10iter: " + str(coverage10))
    # print("총 탐사율 50iter: " + str(coverage50))
    # print("총 탐사율 100iter: " + str(coverage100))
    # print("지나간 노드 개수: " + str(coverage_pass))

    print("agent1 좌표: "+ "x: " + str(agent1_x) + " y: " + str(agent1_y))
    print("agent2 좌표: "+ "x: " + str(agent2_x) + " y: " + str(agent2_y))
    print("agent3 좌표: "+ "x: " + str(agent3_x) + " y: " + str(agent3_y))
    print("knn: " + str(knn_data) + "\nknn 지나간 node 수 : " + str(knn_pass_node)+ "\nknn iter : " + str(knn_iter_count))
    print("프런티어: " + str(frontier_data) + "\n프런티어 지나간 node 수 : " + str(frontier_pass_node) + "\n프런티어 iter : " + str(frontier_iter_count))

    knn_monte_iter = knn_monte_iter + knn_iter_count
    knn_monte_passnode = knn_monte_passnode + knn_pass_node
    frontier_monte_passnode = frontier_monte_passnode + frontier_pass_node
    frontier_monte_iter = frontier_monte_iter + frontier_iter_count

knn_monte_passnode = knn_monte_passnode/n
knn_monte_iter = knn_monte_iter/n
frontier_monte_passnode = frontier_monte_passnode/n
frontier_monte_iter = frontier_monte_iter/n

for iter in range(math.ceil(knn_monte_iter)):
    knn_monte_coverage[iter] = knn_monte_coverage[iter]/n

for iter in range(math.ceil(frontier_monte_iter)):
    frontier_monte_coverage[iter] = frontier_monte_coverage[iter]/n


print("knn iter " + str(math.ceil(knn_monte_iter)) + "\nknn 지나간 node 수 : " + str(math.ceil(knn_monte_passnode)))
print("프런티어 iter: " + str(math.ceil(frontier_monte_iter)) + "\n프런티어 지나간 node 수 : " + str(math.ceil(frontier_monte_passnode)))


#print(knn_monte_iter)
#print(knn_monte_coverage)


knn_monte_iter_list = [i for i in range(math.ceil(knn_monte_iter))]
knn_monte_coverage_list = []
for i in range(len(knn_monte_iter_list)):
    if knn_monte_coverage[i] != 0:
        knn_monte_coverage_list.append(knn_monte_coverage[i])
#plt.plot(knn_monte_iter_list, knn_monte_coverage_list, 'r--')
#plt.plot(frontier_monte_iter, frontier_monte_coverage, 'b--')

# cmap = colors.ListedColormap(['white', 'black'])
# plt.figure(figsize=(6, 6))
# plt.pcolor(map_data[::-1], cmap=cmap, edgecolors='k', linewidths=3)
plt.xlabel('Iteration')
plt.ylabel('Coverage')
plt.legend(['KNN-based', 'Frontier-based'])

cmap = colors.ListedColormap(['white', 'black'])
plt.figure(figsize=(6, 6))
plt.pcolor(map_data3[::-1], cmap=cmap, edgecolors='k', linewidths=3)

plt.axis('off')
plt.show()
# *******************************************************************************************************************************************
