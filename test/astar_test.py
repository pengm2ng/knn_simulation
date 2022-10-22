from resources import astar
from resources import map

map = map.explored_data
start = (6, 11)
end = (6, 11)
path = astar.astar(map, start, end)

print(path)