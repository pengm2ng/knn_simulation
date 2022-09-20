# map의 사이즈를 구하는 함수
def cal_map_size(map_type):
    map_size = len(map_type)
    return map_size

# 탐사 가능한 노드를 탐색하는 함수
# candidate_node_list -> 탐사되어 있는 부분 중 주변에 빈칸이 존재하는 노드와 탐사가능 영역의 개수를 담은 리스트
def find_candidate_node(map_size, explored_data, candidate_node_list):
    for i in range(1, map_size-1):
        for j in range(1, map_size-1):
            if explored_data[i][j] == 3:
                dp = 0
                if explored_data[i][j - 1] == 0:
                    dp = dp + 1
                if explored_data[i][j + 1] == 0:
                    dp = dp + 1
                if explored_data[i + 1][j] == 0:
                    dp = dp + 1
                if explored_data[i - 1][j] == 0:
                    dp = dp + 1
                if explored_data[i - 1][j - 1] == 0:
                    dp = dp + 1
                if explored_data[i + 1][j - 1] == 0:
                    dp = dp + 1
                if explored_data[i + 1][j + 1] == 0:
                    dp = dp + 1
                if explored_data[i - 1][j + 1] == 0:
                    dp = dp + 1

                if dp != 0:
                    dp = 8-dp
                    candidate_node_list.append([i, j, dp])
    return candidate_node_list


#
def set_explored_map(position, explored_data):
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



