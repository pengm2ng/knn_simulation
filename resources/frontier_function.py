import random


# map의 사이즈를 구하는 함수
def cal_map_size(map_type):
    map_size = len(map_type)
    return map_size


# agent의 위치를 무작위로 선정하는
def initialize_agent_position(map_type, explored_map , agent_num):
    initial_position_list = []
    map_size = cal_map_size(map_type)

    for i in range(agent_num):
        while 1:
            ran_num_x = random.randint(1, map_size - 1)
            ran_num_y = random.randint(1, map_size - 1)
            if map_type[ran_num_x][ran_num_y] == 1:
                continue
            else:
                initial_position_list.append([ran_num_x, ran_num_y])
                explored_map[ran_num_x][ran_num_y] = 1
                break

    print("inital agent position: " + str(initial_position_list))
    return initial_position_list


# 탐사 가능한 노드를 탐색하는 함수
# candidate_node_list -> 탐사되어 있는 부분 중 주변에 빈칸이 존재하는 노드와 탐사가능 영역의 개수를 담은 리스트
def find_candidate_node(map_size, explored_data, candidate_node_list, dp_list):
    for i in range(1, map_size - 1):
        for j in range(1, map_size - 1):
            if explored_data[i][j] == 3:
                dp = 0
                if explored_data[i][j - 1] == 9:
                    dp = dp + 1
                if explored_data[i][j + 1] == 9:
                    dp = dp + 1
                if explored_data[i + 1][j] == 9:
                    dp = dp + 1
                if explored_data[i - 1][j] == 9:
                    dp = dp + 1
                if explored_data[i - 1][j - 1] == 9:
                    dp = dp + 1
                if explored_data[i + 1][j - 1] == 9:
                    dp = dp + 1
                if explored_data[i + 1][j + 1] == 9:
                    dp = dp + 1
                if explored_data[i - 1][j + 1] == 9:
                    dp = dp + 1

                if dp != 0:
                    dp = 8 - dp
                    candidate_node_list.append([i, j])
                    dp_list.append(dp)

#
def set_explored_map(position, map_data, explored_data, map_size):
    explored_data[position[0]][position[1]] = 1

    # 8방위 모두 가능한 경우
    if 1 <= position[0] <= map_size - 2 and 1 <= position[1] <= map_size - 2:
        # 오른쪽
        if explored_data[position[0] + 1][position[1]] == 9:
            if map_data[position[0] + 1][position[1]] == 0:
                explored_data[position[0] + 1][position[1]] = 3
            else:
                explored_data[position[0] + 1][position[1]] = 4
        # 왼쪽
        if explored_data[position[0] - 1][position[1]] == 9:
            if map_data[position[0] - 1][position[1]] == 0:
                explored_data[position[0] - 1][position[1]] = 3
            else:
                explored_data[position[0] - 1][position[1]] = 4
        # 아래쪽
        if explored_data[position[0]][position[1] - 1] == 9:
            if map_data[position[0]][position[1] - 1] == 0:
                explored_data[position[0]][position[1] - 1] = 3
            else:
                explored_data[position[0]][position[1] - 1] = 4
        # 위쪽
        if explored_data[position[0]][position[1] + 1] == 9:
            if map_data[position[0]][position[1] + 1] == 0:
                explored_data[position[0]][position[1] + 1] = 3
            else:
                explored_data[position[0]][position[1] + 1] = 4
        # 오른 위
        if explored_data[position[0] + 1][position[1] + 1] == 9:
            if map_data[position[0] + 1][position[1] + 1] == 0:
                explored_data[position[0] + 1][position[1] + 1] = 3
            else:
                explored_data[position[0] + 1][position[1] + 1] = 4
        # 오른 아래
        if explored_data[position[0] + 1][position[1] - 1] == 9:
            if map_data[position[0] + 1][position[1] - 1] == 0:
                explored_data[position[0] + 1][position[1] - 1] = 3
            else:
                explored_data[position[0] + 1][position[1] - 1] = 4
        # 왼 위
        if explored_data[position[0] - 1][position[1] + 1] == 9:
            if map_data[position[0] - 1][position[1] + 1] == 0:
                explored_data[position[0] - 1][position[1] + 1] = 3
            else:
                explored_data[position[0] - 1][position[1] + 1] = 4
        # 왼 아래
        if explored_data[position[0] - 1][position[1] - 1] == 9:
            if map_data[position[0] - 1][position[1] - 1] == 0:
                explored_data[position[0] - 1][position[1] - 1] = 3
            else:
                explored_data[position[0] - 1][position[1] - 1] = 4


def set_explored_passnode(position, explored_data):
    explored_data[position[0]][position[1]] = 2
