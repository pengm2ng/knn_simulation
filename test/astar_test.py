from resources import astar
from resources import map

map = map.explored_data
start = (5, 17)
end = (3, 15)
path = astar.astar(map, start, end)

print(path)