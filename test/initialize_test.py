import random
from resources import map
from resources import frontier_function


map_type = map.map_data1
map_size = 20
explored = map.explored_data
a = frontier_function.initialize_agent_position(map_type,explored,6)

for i in range(6):
    print(map_type[a[i][0]][a[i][1]])