class Agent:

    def __init__(self, x, y, passnode):
        self.x = x
        self.y = y
        self.passnode = passnode
        frontier_node_list = []
        moving_distance_list = []
        self.frontier_node_list = frontier_node_list
        self.moving_distance_list = moving_distance_list

    def get_position(self):
        return self

    def set_position(self, x, y, distance):
        self.x = x
        self.y = y
        self.frontier_node_list.append([self.x, self.y])
        self.moving_distance_list.append(distance)

    def get_passnode(self):
        return self

    def set_passnode(self):
        self.passnode.append([self.x, self.y])