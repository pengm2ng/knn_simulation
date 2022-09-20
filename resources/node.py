class Node:

    def __init__(self, x, y, a, dp):
        self.x = x
        self.y = y
        self.a = a
        self.dp = dp

    def get_astar(self):
        return self.a

    def get_dp(self):
        return self.dp