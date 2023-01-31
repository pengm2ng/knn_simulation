import copy
from time import sleep

from resources import astar, knn_metric, distance
from resources import frontier_function
from resources.agent import Agent
from resources import knn_function
from matplotlib import pyplot as plt
from matplotlib import colors

astar_map = []

def simulate_sibal_knn(agent_num, map_type, explored_data, k, monte_num,init_position):
    # class advanced_knn:
    #     def __int__(self, agent_num, map_type):
    #         self.agent_num = agent_num
    #         self.map_type = map_type
    # 전역 변수
    map_size = frontier_function.cal_map_size(map_type)
    print(map_size)
    k_num_list = []
    total_selected_k = []
    total_time = 0
    total_iter = []
    passnode_length = []
    moving_distance_mean = []
    whole_time = []
    explored_data_temp  = copy.deepcopy(explored_data)
    # 전체 몬테카를로 검증
    for monte in range(1, monte_num + 1):
        change_map_temp = []
        print('\nknn ' + str(monte))
        changed_map = copy.deepcopy(explored_data)

        flag = 1
        explored_data_temp = []
        agent_list = []

        selected_k = []  # 각 iter 마다 선택된 k
        agent_path_length = []  # 각 에이전트의 이동거리
        total_path_length = []  # 전체 이동거리
        simulation_time = []  # 시뮬레이션 시간

        # 랜덤으로 에이전트 위치 생성
        # 단 에이전트가 closed 위치에 존재해서는 안됨.
        init_pos = init_position[monte-1]

        frontier_node_list_x = []
        frontier_node_list_y = []
        for ag in range(agent_num):
            frontier_node_list_x.append([init_pos[ag][0]])
            frontier_node_list_y.append([init_pos[ag][1]])

        # 에이전트 객체 생성 후 탐사 지도에 에이전트 위치 1로 기입
        for ag in range(agent_num):
            explored_data[init_pos[ag][0]][init_pos[ag][1]] = 1
            agent = Agent(init_pos[ag][0], init_pos[ag][1], (init_pos[ag][0], init_pos[ag][1]))
            # print("position" + str(agent.get_position()[1]))
            agent_list.append(agent)

        # print(explored_data)

        iter_cnt = 0

        iter_time = 0
        # coverage가 99%를 넘으면 flag = 0이됨 = 탐사 종료
        while flag:

            time = 0
            candidate_node_list = []
            dp_list = []
            whole_next_node_iter = []
            next_frontier_node = []
            # ?????????????????
            next_frontier_node_list = []
            iter_cnt = iter_cnt + 1
            selected_k = []  # 각 iter 마다 선택된 k

            # 이전에 갔던 노드
            pre_frontier_node = []
            print("\n**********탐사 " + str(monte) + "**********")
            print("**********iter " + str(iter_cnt) + "**********\n")

            for ag in range(agent_num):
                print("agent" + str(ag) + "의 위치:" + str(agent_list[ag].get_position()))

            # agent들이 이동할 수 있는 노드 검색
            # 현재 agent의 위치는 1로표현하며, open된 구연 즉, 이동할 수 있는 노드는 3으로 표시한다.

            # 이미 3으로 된 open space 들을 6으로 바꿔버린다.
            frontier_function.update_open_space(changed_map, map_size)

            for ag in range(agent_num):
                frontier_function.set_explored_map(agent_list[ag].get_position(), map_type, changed_map, map_size)

            # 여기서 문제점 발생 - 이전 이동 가능 노드도 3으로 지정한 것 때문에 모든 것이 candidate node로 들어가 버리게 되어버림
            frontier_function.find_candidate_node(map_size, changed_map, candidate_node_list, dp_list)
            print("candidate node : " + str(candidate_node_list))
            print("dp value : " + str(dp_list))
            # removed_alredy_node = candidate_node_list
            if iter_cnt % 100 == 0:
                cmap = colors.ListedColormap(['red', 'blue', 'grey', 'white', 'green', 'black'])
                plt.figure(figsize=(6, 6))
                plt.pcolor(changed_map[::-1], cmap=cmap, edgecolors='k', linewidths=3)
                plt.axis('off')
                plt.show()
            if len(candidate_node_list) == 0:
                total_iter.append(iter_cnt - 1)
                cmap = colors.ListedColormap(['red', 'blue', 'grey', 'white', 'green', 'black'])
                plt.figure(figsize=(6, 6))
                plt.pcolor(changed_map[::-1], cmap=cmap, edgecolors='k', linewidths=3)
                plt.axis('off')
                plt.show()
                break

            # k 값에 따라 다른 지도양상을 보이므로 explored_temp에 k값만큼 저장한다.
            for k_map in range(k):
                explored_data_temp.append(changed_map)

            # 최단 경로를 찾기 위하여 이동가능 경로를 모두 0으로 바꾼 map을 새롭게 정의
            # candidate node는 k의 값에 상관없이 항상 일정하기 때문에 위에서 한번만 초기화 해주면 됨
            astar_map = copy.deepcopy(changed_map)

            for m in range(map_size):
                for n in range(map_size):
                    if changed_map[m][n] == 3:
                        astar_map[m][n] = 0
                    if changed_map[m][n] == 1:
                        astar_map[m][n] = 0
                    if changed_map[m][n] == 2:
                        astar_map[m][n] = 0
                    if changed_map[m][n] == 6:
                        astar_map[m][n] = 0
                    if changed_map[m][n] == 7:
                        astar_map[m][n] = 0

            # 각각의 k의 가중치합을 담아놓는 리스트
            each_k_weight_list = []

            # knn 몬테카를로 검증
            # 한 iteration마다 최적의 k 값을 뽑아낸다.

            # 각 k마다 탐사 노드를 할당받지 못한 에이전트의 번호를 담는 리스트
            null_agent = []

            k_next_frontier_node = []
            print("\nk=" + str(k) + "일때, 각 에이전트에게 할당된 노드")
            # 에이전트에게 frontier 노드 할당
            training_points = []
            training_labels = []
            knn_metric.get_map(astar_map)
            # 1차 노드를 에이전트에게 할당
            '''
                    knn을 통해서 각 에이전트에게 candidate node를 할당한다.
                      cmap = colors.ListedColormap(['red', 'blue', 'grey', 'white', 'green', 'black'])
            plt.figure(figsize=(6, 6))
            plt.pcolor(changed_map[::-1], cmap=cmap, edgecolors='k', linewidths=3)
            plt.axis('off')
            plt.show()
            '''

            for ag in range(agent_num):
                if iter_cnt >= k:
                    training_points = training_points + agent_list[ag].get_frontier_node()[-k:]
                    for i in agent_list[ag].get_frontier_node()[-k:]:
                        training_labels.append(ag)
                else:
                    training_points = training_points + agent_list[ag].get_frontier_node()[-iter_cnt:]
                    for i in agent_list[ag].get_frontier_node()[-iter_cnt:]:
                        training_labels.append(ag)
            # print("candidate_frontier_node: " + str(candidate_node_list))
            print("training point: " + str(training_points))
            print("training label: " + str(training_labels))
            if len(training_labels) < k*agent_num:
                allocation = knn_function.allocate_frontier_node(iter_cnt, training_points, training_labels,
                                                                 candidate_node_list)
            else:
                if len(candidate_node_list) != 0:
                    allocation = knn_function.allocate_frontier_node(k, training_points, training_labels,
                                                                     candidate_node_list)
            print("할당된 노드: " + str(allocation))


            # knn_function.show_plt(candidate_node_list, allocation, training_points, training_labels,map_type,map_size)
            '''
                    agent_allocated_list: 각 에이전트에 할당된 노드 좌표 리스트 -> [[x1,y1],[x2,y2]...]
                    agent_dp_list: 각 노드의 dp 값 -> [a,b,c,d...]
                    path_length_list: 각에이전트에 할당된 노드와 현재 에이전트의 위치와의 거리
                    new_candidate_node: 이동불가능한 노드를 제외한 노드를 담는 리스트
                '''
            # 노드를 할당받은 에이전트부터 가중치 값을 구한다.
            for ag in range(agent_num):

                agent_allocated_list = []
                agent_dp_list = []
                path_length_list = []
                path_list = []

                new_candidate_node = []  # 이동불가능한 노드를 제외한 새로운 변수
                new_candidate_node_dp = []

                for al in range(len(allocation)):
                    if allocation[al] == ag:
                        agent_allocated_list.append(candidate_node_list[al])
                        agent_dp_list.append(dp_list[al])
                # print("\nagent" + str(ag) + "에 할당된 노드: " + str(agent_allocated_list))
                # print("agent" + str(ag) + "에 할당된 노드의 dp: " + str(agent_dp_list))

                '''
                     각 에이전트가 할당된 frontier 노드를 바탕으로 최단 경로 탐색하여 각 노드에 값 저장
                     각 에이전트가 할당된 frontier 노드를 바탕으로 dp 값을 계산하여 각 노드에 값 저장
                '''

                if len(agent_allocated_list) != 0:
                    for des in range(len(agent_allocated_list)):

                        start = (agent_list[ag].get_position()[0], agent_list[ag].get_position()[1])
                        end = (agent_allocated_list[des][0], agent_allocated_list[des][1])
                        print("노드 저장완료")
                        path = astar.astar(astar_map, start, end)
                        print("탐색 끝")
                        if str(type(path)) != "<class 'NoneType'>":
                            path_list.append(path)
                            path_length_list.append(len(path) - 1)
                            new_candidate_node.append((agent_allocated_list[des][0], agent_allocated_list[des][1]))
                            new_candidate_node_dp.append(agent_dp_list[des])

                #print("agent" + str(ag) + "에 할당된 이동가능한 노드: " + str(new_candidate_node))
                #print("agent" + str(ag) + "에 할당된 노드의 dp: " + str(new_candidate_node_dp))
                #print("agent" + str(ag) + "에 할당된 노드까지의 path_length: " + str(path_length_list))
                #print("agent" + str(ag) + "에 할당된 노드까지의 path: " + str(path_list))

                '''
                    이동가능한 노드가 존재하는 경우
                     agent_final_candidate: 최저의 가중치 값을 가진 좌표 후보
                    final_candidate_weight: 그때의 가중치 값
                '''
                if len(new_candidate_node) != 0:

                    agent_final_candidate = []
                    min_path = min(path_length_list)
                    k_next_frontier_node_temp = []
                    for w in range(len(path_length_list)):
                            weight = new_candidate_node_dp[w], path_length_list[w];
                            agent_final_candidate.append(new_candidate_node[w])
                            eu_dist = distance.euclidean(agent_list[ag].get_position(),new_candidate_node[w])
                            k_next_frontier_node_temp.append([new_candidate_node[w], ag, new_candidate_node_dp[w], path_length_list[w], path_list[w],eu_dist])
                            print([new_candidate_node[w], ag, new_candidate_node_dp[w], path_length_list[w], path_list[w]])
                    k_next_frontier_node_temp.sort(key=lambda k_next_frontier_node_temp: (k_next_frontier_node_temp[1],k_next_frontier_node_temp[3],k_next_frontier_node_temp[4]))
                    for e in k_next_frontier_node_temp:
                        print(e)
                    k_next_frontier_node.append(k_next_frontier_node_temp[0])

                if len(new_candidate_node) == 0:
                    null_agent.append(ag)

                '''
                    노드를 할당 받지 못한 노드들의 가중치를 구한다.
                '''
            # 각 에이전트에 할당된 frontier 노드의 변수들을 가중치 값을 적용하여 가장 작은 노드 선정
            print("1차 할당 후 후보군들 :" + str(k_next_frontier_node))
            print("할당받지 못한 agent: " + str(null_agent))
            for n in null_agent:
                k_next_frontier_node.append([agent_list[n].get_position(), n, 0, 0, []])
                print([agent_list[n].get_position(), n, 0, 0, []])

            k_next_frontier_node.sort(key=lambda k_next_frontier_node: (k_next_frontier_node[1]))
            print("k= " + str(k) + "일때의 다음 노드 최종 후보군들: " + str(k_next_frontier_node))
            agent_num = 0

            final_node = []
            for e in k_next_frontier_node:
                print(e)

            agent_num = 0
            for i, v in enumerate(k_next_frontier_node):
                if v[1] == agent_num:
                    final_node.append(v)
                    agent_num = agent_num + 1
            print("최종 노드 : " + str(final_node))


            for ag in range(agent_num):
                start = (agent_list[ag].get_position()[0], agent_list[ag].get_position()[1])
                end = (final_node[ag][0][0], final_node[ag][0][1])

                path = astar.astar(astar_map, start, end)
                # length = 0
                if str(type(path)) == "<class 'NoneType'>":
                    print("**********************************************************" + str(start))
                    print(end)

                else:
                    length = len(path) - 1
                print("agent" + str(ag) + ": [" + str(agent_list[ag].get_position()[0]) + " ," + str(
                    agent_list[ag].get_position()[1]) + "] 에서")
                print("agent" + str(ag) + ": [" + str(final_node[ag][0][0]) + " ," + str(
                    final_node[ag][0][1]) + "] 로" + str(length) + "만큼 이동")
                frontier_function.set_explored_passnode(agent_list[ag].get_position(), changed_map)

                agent_list[ag].set_position(final_node[ag][0][0], final_node[ag][0][1], length, path)

                if time < agent_list[ag].get_moving_distance_list()[iter_cnt - 1]:
                    print(agent_list[ag].get_moving_distance_list()[iter_cnt - 1])
                    time = agent_list[ag].get_moving_distance_list()[iter_cnt - 1]
                print("time" + str(time))
            iter_time = iter_time + time
            print("iter_time" + str(iter_time))

        for ag in range(agent_num):
            explored_data[init_pos[ag][0]][init_pos[ag][1]] = 9
        whole_time.append(iter_time)
        print("whole_time" + str(whole_time))
        for ag in range(agent_num):
            passnode = agent_list[ag].get_frontier_node()
            passnode_length.append(len(passnode))
            moving_distance = agent_list[ag].get_moving_distance_list()
            moving_distance_mean.append(sum(moving_distance))
            print(moving_distance_mean)
            print(passnode_length)

        print(agent_list[1].get_frontier_node())

        for ag in range(agent_num):

            for n,v in enumerate(agent_list[ag].get_frontier_node()):
                print(v)

                frontier_node_list_x[ag].append(v[0])
                frontier_node_list_y[ag].append(v[1])

    print("##################################3")
    color = ['bs', 'ms', 'ys', 'gs', 'ks', 'rs']
    print(agent_list[0].get_frontier_node())
    for ag in range(agent_num):
        for map_count1 in range(20):
            for map_count2 in range(20):
                if map_type[map_count1][map_count2] == 1:
                    plt.plot(map_count1, map_count2, 'ks', markersize=8)
        x1 = frontier_node_list_x[ag]
        y1 = frontier_node_list_y[ag]
        print(x1)
        print(y1)
        plt.plot(x1, y1, color[ag], marker='o', markersize=8, label='agent ' + str(ag + 1))
        plt.axis([-1, 20, -1, 20])

        plt.grid(True)
        plt.xticks(range(21))
        plt.yticks(range(21))
    for ag in range(agent_num):
        plt.plot(init_position[0][ag][0], init_position[0][ag][1], 'rs', markersize=9)

    plt.legend(loc='upper right')
    plt.xlabel('X-Axis')
    plt.ylabel('Y-Axis')
    plt.show()

    passnode_mean = []
    moving_distance_mean_mean = []
    total_time = sum(whole_time) / monte_num
    for ag in range(agent_num):
        passnode_mean.append(0)
        moving_distance_mean_mean.append(0)

    for n in range(len(passnode_length)):
        i = n % agent_num
        passnode_mean[i] = passnode_mean[i] + passnode_length[n]
        moving_distance_mean_mean[i] = moving_distance_mean[n] + moving_distance_mean_mean[i]

    for ag in range(agent_num):
        passnode_mean[ag] = passnode_mean[ag] / monte_num
        moving_distance_mean_mean[ag] = moving_distance_mean_mean[ag] / monte_num
        print("agent" + str(ag) + "의 frontier_node 평균 : " + str(passnode_mean[ag] - 1))
        print("agent" + str(ag) + "의 moving_distance 평균 : " + str(moving_distance_mean_mean[ag]))

    iter_mean = sum(total_iter) / monte_num
    print(total_iter)
    print("평균 iter : " + str(iter_mean))
    print("평균 time : " + str(total_time))


    #f = open("C:/Users/장인호/Desktop/knn_simulation/result/total.txt", 'a')
    #f = open("D:/knn_simulation/sibal531.txt", 'a')
    #f.write("k= " + str(k) + "  ")
    #f.write("agent_num= " + str(agent_num) + "  ")
    #f.write("monte_num= " + str(monte_num) + "\n\n")


    #f.write("평균 iter : " + str(iter_mean) + "\n")
    #f.write("평균 time : " + str(total_time) + "\n\n")
    #f.close()
    return_value = []
    for ag in range(agent_num):
        return_value.append(moving_distance_mean_mean[ag])
    return_value.append(total_time)
    return_value.append(iter_mean)
    return return_value













'''




'''