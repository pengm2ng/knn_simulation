class Agent:

    def __init__(self, x, y, passnode):
        self.x = x
        self.y = y
        self.passnode = passnode
        frontier_node_list = []
        moving_distance_list = []
        moving_path_list = []
        self.frontier_node_list = [(self.x, self.y)]
        self.moving_distance_list = moving_distance_list
        self.moving_path_list = moving_path_list

    def get_position(self):
        return (self.x, self.y)

    def set_position(self, x, y,distance,path):
        self.x = x
        self.y = y
        self.frontier_node_list.append((self.x, self.y))
        self.moving_distance_list.append(distance)
        self.moving_path_list.append(path)

    def get_passnode(self):
        # passnode => 전체 지나간 좌표
        return self.passnode

    def set_passnode(self):
        self.passnode.append([self.x, self.y])

    def get_frontier_node(self):
        return self.frontier_node_list

    def get_moving_distance_list(self):
        return self.moving_distance_list

    def get_moving_path_list(self):
        return self.moving_path_list