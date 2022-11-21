import copy
from time import sleep

from resources import astar, distance
from resources import frontier_function
from resources.agent import Agent
from resources import knn_function
from matplotlib import pyplot as plt
from matplotlib import colors

def simulate_voronoi(agent_num, map_type, explored_data,k,monte_num,init_position):
    # class advanced_knn:
    #     def __int__(self, agent_num, map_type):
    #         self.agent_num = agent_num
    #         self.map_type = map_type
    # 전역 변수
    map_size = frontier_function.cal_map_size(map_type)
    k_num_list = []
    total_selected_k = []
    total_time = 0
    total_iter = []
    passnode_length = []
    moving_distance_mean = []
    whole_time = []




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
            agent = Agent(init_pos[ag][0], init_pos[ag][1], [[init_pos[ag][0]], init_pos[ag][1]])
            # print("position" + str(agent.get_position()[1]))
            agent_list.append(agent)

        # print(explored_data)
        astar_map = []
        iter_cnt = 0

        iter_time = 0

        # coverage가 99%를 넘으면 flag = 0이됨 = 탐사 종료
        while flag:
            agent_candidate_node_list = []
            for ag in range(agent_num):
                agent_candidate_node_list.append([ag])
            voronoi_map = copy.deepcopy(map_type)
            candidate_points = []

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

            for i in range(map_size):
                for j in range(map_size):
                    if changed_map[i][j] !=1:
                        candidate_points.append((i, j))
            # 여기서 문제점 발생 - 이전 이동 가능 노드도 3으로 지정한 것 때문에 모든 것이 candidate node로 들어가 버리게 되어버림
            frontier_function.find_candidate_node(map_size, changed_map, candidate_node_list, dp_list)
            print("candidate node : " + str(candidate_node_list))
            print("dp value : " + str(dp_list))
            # removed_alredy_node = candidate_node_list
            if iter_cnt % 100 == 0:
                cmap = colors.ListedColormap(['red', 'blue', 'yellow', 'white', 'green', 'black'])
                plt.figure(figsize=(6, 6))
                plt.pcolor(changed_map[::-1], cmap=cmap, edgecolors='k', linewidths=3)
                plt.axis('off')
                plt.show()

            if len(candidate_node_list) == 0:
                total_iter.append(iter_cnt - 1)
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

            # 1차 노드를 에이전트에게 할당
            '''
                    knn을 통해서 각 에이전트에게 candidate node를 할당한다.
            '''
            for ag in range(agent_num):
                    training_points.append(agent_list[ag].get_position())
                    training_labels.append(ag)
                # print("candidate_frontier_node: " + str(candidate_node_list))

            print("training point: " + str(training_points))
            print("training label: " + str(training_labels))
            print("candidate points: " + str(candidate_points))

            allocation = knn_function.allocate_frontier_node(1, training_points, training_labels,candidate_points)
            print("할당된 노드: " + str(allocation))
            for w in range(len(candidate_points)):
                voronoi_map[candidate_points[w][0]][candidate_points[w][1]] = allocation[w]+1
            '''
            cmap = colors.ListedColormap(['red', 'blue', 'yellow', 'white', 'green', 'black','green', 'yellow', 'blue'])
            plt.figure(figsize=(6, 6))
            plt.pcolor(voronoi_map[::-1], cmap=cmap, edgecolors='k', linewidths=3)
            plt.axis('off')
            plt.show()
            '''

            for w in range(len(allocation)):
                for ag in range(agent_num):
                    if allocation[w] == ag and changed_map[candidate_points[w][0]][candidate_points[w][1]] == 3:
                        agent_candidate_node_list[ag].append([candidate_points[w][0],candidate_points[w][1]])

            print("이동가능한 노드:"+ str(agent_candidate_node_list))
            path_length_list = []
            non_selected =[]
            for al in range(agent_num):
                min = 9999999
                path_length_list.append([al])
                # agent 0
                if len(agent_candidate_node_list[al]) == 1:
                    continue
                else:
                    for w in range(1, len(agent_candidate_node_list[al])):
                        distance_agent_node = distance.euclidean(agent_list[al].get_position(),agent_candidate_node_list[al][w])
                        distance_init_node = distance.euclidean(agent_list[al].get_frontier_node()[0],agent_candidate_node_list[al][w])
                        print("초기위치" + str(agent_list[al].get_frontier_node()[0]))
                        omega =distance_agent_node + distance_init_node
                        if min > omega:
                            node = [agent_candidate_node_list[al][w][0],agent_candidate_node_list[al][w][1]]
                            min = omega
                            agent_path = omega


                        else:
                            non_selected.append([agent_candidate_node_list[al][w][0],agent_candidate_node_list[al][w][1]])
                    path_length_list[al].append(node)
                    path_length_list[al].append(agent_path)
                    path_length_list[al].append(0)
                    agent_candidate_node_list[al].remove(node)
            print(agent_candidate_node_list)

            print("1차 후보" + str(path_length_list))

            for al in range(agent_num):
                if len(agent_candidate_node_list[al]) == 1:
                    continue
                else:

                    for w in range(1, len(agent_candidate_node_list[al])):
                        print(1)
                        print([agent_candidate_node_list[al][w][0],agent_candidate_node_list[al][w][1]])
                        non_selected.append([agent_candidate_node_list[al][w][0],agent_candidate_node_list[al][w][1]])

            if iter_cnt % 100 == 0:
                cmap = colors.ListedColormap(['red', 'blue', 'yellow', 'white', 'green', 'purple'])
                plt.figure(figsize=(6, 6))
                plt.pcolor(voronoi_map[::-1], cmap=cmap, edgecolors='k', linewidths=3)
                plt.axis('off')
                plt.show()


            for ag in range(agent_num):
                print("agent" + str(ag) + ": [" + str(agent_list[ag].get_position()[0]) + " ," + str(agent_list[ag].get_position()[1]) + "] 에서")
                #print("agent" + str(ag) + ": [" + str(final_node[ag][0][0]) + " ," + str(final_node[ag][0][1]) + "] 로" + str(length) + "만큼 이동")
                frontier_function.set_explored_passnode(agent_list[ag].get_position(), changed_map)
                agent_list[ag].set_position(path_length_list[ag][1][0], path_length_list[ag][1][1], path_length_list[ag][2], path_length_list[ag][3])

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

        for ag in range(agent_num):

            for n, v in enumerate(agent_list[ag].get_frontier_node()):
                print(v)
                print(v[0])
                frontier_node_list_x[ag].append(v[0])
                frontier_node_list_y[ag].append(v[1])


    color = ['bs-', 'rs-', 'ys-', 'ks-', 'ys', 'os']
    print(agent_list[0].get_frontier_node())
    for ag in range(agent_num):
        x1 = frontier_node_list_x[ag]
        y1 = frontier_node_list_y[ag]
        print(x1)
        print(y1)
        plt.plot(x1, y1, color[ag])
        plt.axis([0, 20, 0, 20])

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

    f = open("C:/Users/장인호/Desktop/knn_simulation/result/kimst_map1_temp.txt", 'a')
    #f = open("D:/knn_simulation/default531.txt", 'a')
    f.write("k= " + str(k) + "  ")
    f.write("agent_num= " + str(agent_num) + "  ")
    f.write("monte_num= " + str(monte_num) + "\n\n")

    for ag in range(agent_num):

        f.write("agent" + str(ag) + "의 moving_distance 평균 : " + str(moving_distance_mean_mean[ag]) + "\n")
    f.write("평균 iter : " + str(iter_mean) + "\n")
    f.write("평균 time : " + str(total_time) + "\n\n")
    f.close()

'''
                


            
'''