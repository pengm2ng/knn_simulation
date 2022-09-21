# class advanced_knn:
#     def __int__(self, agent_num, map_type):
#         self.agent_num = agent_num
#         self.map_type = map_type
from resources import astar
from resources import frontier_function
from resources import agent
from resources.agent import Agent


def simulate_advanced_knn(agent_num, map_type, explored_data, k_num, monte_num, ):
    # 전역 변수
    map_size = frontier_function.cal_map_size(map_type)

    # 전체 몬테카를로 검증
    for monte in range(1, monte_num+1):
        print('advanced_knn ' + str(monte))

        flag = 1
        explored_data_temp = []
        agent_list = []

        # 매 iteration 마다 k에 따른 최적의 좌표를 뽑기 때문에 explored_data 사본을 k값 만큼 뽑는다.
#        for k in range(k_num):
#            explored_data_temp[k] = explored_data


        # 랜덤으로 에이전트 위치 생성
        # 단 에이전트가 closed 위치에 존재해서는 안됨.
        init_pos = frontier_function.initialize_agent_position(map_type, explored_data, agent_num)

        # 에이전트 객체 생성
        for ag in range(agent_num):
            agent[ag] = Agent(init_pos[ag][0], init_pos[ag][1], [])
            agent_list.append(agent)
        print(explored_data)

        # coverage가 99%를 넘으면 flag = 0이됨 = 탐사 종료
        while flag:

            #?????????????????
            cnt = 0
            cnt = cnt + 1

            # 이전에 갔던 노드
            pre_frontier_node = []


            # agent들이 이동할 수 있는 노드 검색
            for ag in range(agent_num):
                frontier_function.set_explored_map(agent_list[ag].Agent.get_position(), map_type, explored_data_temp, map_size)


            # knn 몬테카를로 검증
            # 한 iteration마다 최적의 k 값을 뽑아낸다.
            # for k in range(1, k_num+1):

                # frontier 노드 검색


                # 에이전트에게 frontier 노드 할당


                # 각 에이전트가 할당된 frontier 노드를 바탕으로 최단 경로 탐색하여 각 노드에 값 저장


                # 각 에이전트가 할당된 frontier 노드를 바탕으로 dp 값을 계산하여 각 노드에 값 저장


                # 각 에이전트에 할당된 frontier 노드의 변수들을 가중치 값을 적용하여 가장 작은 노드 선정


                # agent 가중치 리스트에 저장


                # 에이전트가 새롭게 이동한 위치도 리스트로 저장




                # 최단거리 구하기
                # for문을 통해 최단 거리를 가진 노드를 갱신해서 최종적으로 path의 길이가 작은 end를 출력
               # for i in range(1, ):
               #     path = astar.astar(map_type, start, end)

        flag = 0
