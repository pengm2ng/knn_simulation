from resources import astar_metric_function
from resources import map

map = map.explored_data
start = (5, 17)
end = (3, 15)
path = astar_metric_function.astar(map, start, end)

print(path)