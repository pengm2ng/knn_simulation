class Agent:


    passnode
    def __init__(self, x, y, passnode):
        self.x = x
        self.y = y
        self.passnode = passnode

    def get_position(self):
        return self

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_passnode(self):
        return self

    def set_passnode(self):
        self.passnode.append([self.x, self.y])





