# class advanced_knn:
#     def __int__(self, agent_num, map_type):
#         self.agent_num = agent_num
#         self.map_type = map_type
from resources import astar
from resources import frontier_function
from resources.agent import Agent
from resources import knn_function
from matplotlib import pyplot as plt
from matplotlib import colors
from operator import itemgetter

from resources.frontier_function import distance


def simulate_advanced_knn(agent_num, map_type, explored_data, k_num, monte_num, w1, w2):
    # 전역 변수
    map_size = frontier_function.cal_map_size(map_type)
    k_num_list = []
    total_selected_k = []
    total_agent_path_length = []
    total_time = []
    # 전체 몬테카를로 검증
    for monte in range(1, monte_num + 1):
        print('advanced_knn ' + str(monte))
        changed_map = explored_data
        flag = 1
        explored_data_temp = []
        agent_list = []

        selected_k = [] #각 iter 마다 선택된 k
        agent_path_length = [] # 각 에이전트의 이동거리
        total_path_length = [] # 전체 이동거리
        simulation_time = [] # 시뮬레이션 시간

        # 랜덤으로 에이전트 위치 생성
        # 단 에이전트가 closed 위치에 존재해서는 안됨.
        init_pos = frontier_function.initialize_agent_position(map_type, changed_map, agent_num)

        # 에이전트 객체 생성 후 탐사 지도에 에이전트 위치 1로 기입
        for ag in range(agent_num):
            agent = Agent(init_pos[ag][0], init_pos[ag][1], [[init_pos[ag][0]], init_pos[ag][1]])
            # print("position" + str(agent.get_position()[1]))
            agent_list.append(agent)

        # print(explored_data)

        iter_cnt = 0
        # coverage가 99%를 넘으면 flag = 0이됨 = 탐사 종료
        while flag:
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
            for ag in range(agent_num):
                frontier_function.set_explored_map(agent_list[ag].get_position(), map_type, changed_map, map_size)

            frontier_function.find_candidate_node(map_size, changed_map, candidate_node_list, dp_list)
            print("candidate node : " + str(candidate_node_list))
            print("dp value : " + str(dp_list))
            # removed_alredy_node = candidate_node_list
            if iter_cnt % 10 ==0:
                cmap = colors.ListedColormap(['white', 'red', 'yellow', 'green', 'blue', 'black'])
                plt.figure(figsize=(6, 6))
                plt.pcolor(changed_map[::-1], cmap=cmap, edgecolors='k', linewidths=3)
                plt.axis('off')
                plt.show()
            if len(candidate_node_list) == 0:
                print(iter_cnt)
                break

            # k 값에 따라 다른 지도양상을 보이므로 explored_temp에 k값만큼 저장한다.
            for k_map in range(k_num):
                explored_data_temp.append(changed_map)
            # cmap = colors.ListedColormap(['white', 'red', 'yellow', 'green', 'blue', 'black'])
            # plt.figure(figsize=(6, 6))
            # plt.pcolor(changed_map[::-1], cmap=cmap, edgecolors='k', linewidths=3)
            # plt.axis('off')
            # plt.show()

            # 최단 경로를 찾기 위하여 이동가능 경로를 모두 0으로 바꾼 map을 새롭게 정의
            # candidate node는 k의 값에 상관없이 항상 일정하기 때문에 위에서 한번만 초기화 해주면 됨
            astar_map = changed_map
            for m in range(map_size):
                for n in range(map_size):
                    if changed_map[m][n] == 3:
                        astar_map[m][n] = 0
                    if changed_map[m][n] == 1:
                        astar_map[m][n] = 0
                    if changed_map[m][n] == 2:
                        astar_map[m][n] = 0

            # 각각의 k의 가중치합을 담아놓는 리스트
            each_k_weight_list = []

            # knn 몬테카를로 검증
            # 한 iteration마다 최적의 k 값을 뽑아낸다.


            for k in range(1, k_num + 1):

                if iter_cnt * agent_num < k:
                    break;
                # 각 k마다 탐사 노드를 할당받지 못한 에이전트의 번호를 담는 리스트
                null_agent = []
                #
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

                    training_points = training_points + agent_list[ag].get_frontier_node()
                    for i in agent_list[ag].get_frontier_node():
                        training_labels.append(ag)
                # print("candidate_frontier_node: " + str(candidate_node_list))
                # print("training point: " + str(training_points))
                # print("training label: " + str(training_labels))
                if len(training_labels) < k:
                    break
                else:
                    if len(candidate_node_list) != 0:
                        allocation = knn_function.allocate_frontier_node(k, training_points, training_labels,
                                                                     candidate_node_list)
                    #print("할당된 노드: " + str(allocation))


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
                    weight_list = []
                    new_candidate_node = []  # 이동불가능한 노드를 제외한 새로운 변수
                    new_candidate_node_dp = []

                    for al in range(len(allocation)):
                        if allocation[al] == ag:
                            agent_allocated_list.append(candidate_node_list[al])
                            agent_dp_list.append(dp_list[al])
                    #print("\nagent" + str(ag) + "에 할당된 노드: " + str(agent_allocated_list))
                    #print("agent" + str(ag) + "에 할당된 노드의 dp: " + str(agent_dp_list))


                    '''
                         각 에이전트가 할당된 frontier 노드를 바탕으로 최단 경로 탐색하여 각 노드에 값 저장
                         각 에이전트가 할당된 frontier 노드를 바탕으로 dp 값을 계산하여 각 노드에 값 저장
                    '''
                    if len(agent_allocated_list) != 0:
                        for des in range(len(agent_allocated_list)):

                            start = (agent_list[ag].get_position()[0], agent_list[ag].get_position()[1])
                            end = (agent_allocated_list[des][0], agent_allocated_list[des][1])
                            path = astar.astar(astar_map, start, end)

                            if str(type(path)) != "<class 'NoneType'>":
                                path_list.append(path)
                                path_length_list.append(len(path) - 1)
                                new_candidate_node.append([agent_allocated_list[des][0], agent_allocated_list[des][1]])
                                new_candidate_node_dp.append(agent_dp_list[des])

                        for des in range(len(new_candidate_node)):
                            weight = (w1 * path_length_list[des]) + (w2 * new_candidate_node_dp[des])
                            weight_list.append(weight)

                    print("agent" + str(ag) + "에 할당된 이동가능한 노드: " + str(new_candidate_node))
                    print("agent" + str(ag) + "에 할당된 노드의 dp: " + str(new_candidate_node_dp))
                    print("agent" + str(ag) + "에 할당된 노드까지의 path_length: " + str(path_length_list))
                    print("agent" + str(ag) + "에 할당된 노드까지의 path: " + str(path_list))
                    print("agent" + str(ag) + "에 할당된 노드들의 가중치: " + str(weight_list))

                    '''
                        이동가능한 노드가 존재하는 경우
                         agent_final_candidate: 최저의 가중치 값을 가진 좌표 후보
                        final_candidate_weight: 그때의 가중치 값
                    '''
                    if len(new_candidate_node) != 0:

                        agent_final_candidate = []
                        min_weight = min(weight_list)

                        for w in range(len(weight_list)):
                            if weight_list[w] == min_weight:
                                agent_final_candidate.append(new_candidate_node[w])
                                k_next_frontier_node.append([new_candidate_node[w], ag, min_weight])

                    if len(new_candidate_node) == 0:
                        null_agent.append(ag)

                '''
                    노드를 할당 받지 못한 노드들의 가중치를 구한다.
                '''
                # 각 에이전트에 할당된 frontier 노드의 변수들을 가중치 값을 적용하여 가장 작은 노드 선정
                print("1차 할당 후 후보군들 :" + str(k_next_frontier_node))
                print("할당받지 못한 agent: " + str(null_agent))
                # removed_alredy_node = [] # 할당된 노드를 제외한 나머지 노드
                # removed_already_dp = [] # 그 노드들의 dp
                #
                # '''
                #     removed_already_node에 할당되지 않은 노드를 담는다.
                # '''
                # for r in range(len(candidate_node_list)):
                #     cnt = 0
                #     for f in range(len(k_next_frontier_node)):
                #         if candidate_node_list[r][0] == k_next_frontier_node[f][0][0] and candidate_node_list[r][1] == k_next_frontier_node[f][0][1]:
                #             cnt = cnt + 1
                #     # print(cnt)
                #     if cnt == 0:
                #         removed_alredy_node.append(candidate_node_list[r])
                #         removed_already_dp.append(dp_list[r])





                for ag in range(len(null_agent)):

                    removed_alredy_node = []
                    removed_already_dp = []



                    for r in range(len(candidate_node_list)):
                        cnt = 0
                        for f in range(len(k_next_frontier_node)):
                            if candidate_node_list[r][0] == k_next_frontier_node[f][0][0] and candidate_node_list[r][1] == k_next_frontier_node[f][0][1]:
                                cnt = cnt + 1
                        # print(cnt)
                        if cnt == 0:
                            removed_alredy_node.append(candidate_node_list[r])
                            removed_already_dp.append(dp_list[r])
                    length_temp = len(removed_alredy_node)
                    non_selected_agent_node = []
                    non_selected_agent_path = []
                    non_selected_agent_path_length = []
                    non_selected_agent_node_dp = []
                    weight_list = []
                    for n in range(length_temp):
                        start = (agent_list[ag].get_position()[0], agent_list[ag].get_position()[1])

                        end = (removed_alredy_node[n][0], removed_alredy_node[n][1])

                        path = astar.astar(astar_map, start, end)

                        if str(type(path)) != "<class 'NoneType'>":
                            non_selected_agent_path.append(path)
                            non_selected_agent_path_length.append(len(path) - 1)
                            non_selected_agent_node.append([removed_alredy_node[n][0], removed_alredy_node[n][1]])
                            non_selected_agent_node_dp.append(removed_already_dp[n])

                            # del removed_alredy_node(removed_alredy_node.index(n))
                            # del removed_already_dp(removed_alredy_node.index(n))
                    for des in range(len(non_selected_agent_node)):
                        weight = w1 * non_selected_agent_path_length[des] + w2 * non_selected_agent_node_dp[des]
                        weight_list.append(weight)

                    print("agent" + str(null_agent[ag]) + "에 재할당된 노드들의 가중치: " + str(weight_list))

                    if len(weight_list) == 0:
                        k_next_frontier_node.append([[agent_list[null_agent[ag]].get_position()[0],
                                                      agent_list[null_agent[ag]].get_position()[1]], null_agent[ag], 0])
                    else :
                        min_weight = min(weight_list)
                        for w in range(len(weight_list)):
                            if weight_list[w] == min_weight:
                                agent_final_candidate.append(non_selected_agent_node[w])
                                k_next_frontier_node.append([non_selected_agent_node[w], null_agent[ag], min_weight])





                print("k= " + str(k) + "일때의 다음 노드 최종 후보군들: " + str(k_next_frontier_node))


                '''
                 agent 내림차순 정렬
                '''
                k_next_frontier_node.sort(key=lambda k_next_frontier_node: k_next_frontier_node[1])


                '''
                    선정된 노드 후보군을 바탕으로 k값이 가장 작은 값과 프론티어 노드를 선정
                    현재 k_next_frontier_node 는 후보로 선정된 여러개의 노드들이 있다.
                    에이전트가 중복되어서 선정되어있다.
                    그러므로 0,1,2,3을 하나씩만 추려내야한다.
                    어짜피 4개면 상관없지만, 00 11 22 33 이라하면 이 안에서도 최적의 조건을 찾아야한다.
                    1. 효율이 높은 노드 4개를 선정한다.
                    2. weight를 모두 더한다.
                    3. 최종 노드 리스트에 입력한다.
                    4. 또한 충돌방지를 위하여 각 uav이 이동경로를 확인한다.
                    5. 이동경로와 이동거리를 토대로 총 이동시간을 합산하고
                    6. 이동경로가 겹칠경우 해당 이동거리가 적은 uav는 잠시 stop 한다
                    
                    selected_k = [] #각 iter 마다 선택된 k
                    agent_path_length = [] # 각 에이전트의 이동거리 
                    total_path_length = [] # 전체 이동거리
                    simulation_time = [] # 시뮬레이션 시간 
                '''
                weight_sum = 0
                agent_node_partition = []
                agent_node_list = []
                agent_number = 0;
                prev_agent_number = -1;

                agent_number =0

                for i in range(len(k_next_frontier_node)):
                    if k_next_frontier_node[i][1] == agent_number:
                        agent_node_list.append(k_next_frontier_node[i])
                        weight_sum=weight_sum + k_next_frontier_node[i][2]
                        agent_number = agent_number+1


                print("k=" + str(k) + "일때 다음 프론티어 노드: " + str(agent_node_list))
                print("k=" + str(k) + "일때 총 가중치 합: " + str(weight_sum))

                '''
                    weight 총정리 하여 최종이동 노드 선정
                '''
                selected_k.append([k, weight_sum])
                print("현재까지의 [k, k일때의 weight_sum]: " + str(selected_k))
                whole_next_node_iter.append([k, agent_node_list[0], agent_node_list[1], agent_node_list[2], agent_node_list[3]])

            selected_k.sort(key=lambda selected_k: selected_k[1])
            final_node = []
            final_k = []

            if selected_k[0][0] != 1:
                final_k.append([selected_k[0][0], selected_k[0][1]])
                print(final_k)
            else:
                final_k.append([selected_k[1][0], selected_k[1][1]])
                print(final_k)

            for i in range(len(whole_next_node_iter)):
                if whole_next_node_iter[i][0] == final_k[0][0]:
                    final_node.append(whole_next_node_iter[i])
                    break;
            print("선택된 최종 노드: "+ str(final_node))



            for ag in range(agent_num):
                start = (agent_list[ag].get_position()[0], agent_list[ag].get_position()[1])
                end = (final_node[0][ag+1][0][0], final_node[0][ag+1][0][1])

                path = astar.astar(changed_map, start, end)
                # length = 0
                if str(type(path)) == "<class 'NoneType'>":
                        print("**********************************************************" + str(start))
                        print(end)

                else:
                        length = len(path) - 1
                print("agent"+str(ag)+": [" + str(agent_list[ag].get_position()[0]) + " ,"+ str(agent_list[ag].get_position()[1]) + "] 에서")
                print("agent"+str(ag)+": [" + str(final_node[0][ag+1][0][0]) + " ,"+ str(final_node[0][ag+1][0][1]) + "] 로 이동")
                agent_list[ag].set_position(final_node[0][ag+1][0][0], final_node[0][ag+1][0][1], length)
                frontier_function.set_explored_passnode(agent_list[ag].get_position(), changed_map)



