# class advanced_knn:
#     def __int__(self, agent_num, map_type):
#         self.agent_num = agent_num
#         self.map_type = map_type
from resources import astar


flag = 1


def simulate_advanced_knn(agent_num, map_type, explored_data):
    for monte in range(1, 101):
        print('advanced_knn '+str(monte))
        for k in range(1, 11):
            cnt = 0
            while flag:
                cnt = cnt + 1


                # 최단거리 구하기
                # for문을 통해 최단 거리를 가진 노드를 갱신해서 최종적으로 path의 길이가 작은 end를 출력
                for i in range(1,):
                    path = astar.astar(map_type, start, end)





















                if flag == 0:
                    break



