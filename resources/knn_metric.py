import copy
import re

from resources import astar_metric_function, astar
from resources import map
import sibal_knn
import sibal_knn

map_temp = []

def get_map(astar_map):
    global cnt
    cnt = 0
    print("받아온 map")

    global map_temp
    map_temp = copy.deepcopy(astar_map)



def astar_metric(x,y):



    print(x, y)
    num_x1 = re.sub(r'[^0-9]', '', str(x[0]))
    num_x2 = re.sub(r'[^0-9]', '', str(x[1]))
    num_y1 = re.sub(r'[^0-9]', '', str(y[0]))
    num_y2 = re.sub(r'[^0-9]', '', str(y[1]))



    new_x = (int(num_x1[0:-1]), int(num_x2[0:-1]))
    new_y = (int(num_y1[0:-1]), int(num_y2[0:-1]))
    if new_y[0] > 20 or new_x[0] >20 or new_y[1] > 20 or new_x[1] >20:
        return 9999999999999999999
    print(new_x, new_y)

    path = astar.astar(map_temp, new_y,new_x)


    print(path)
    if str(type(path)) != "<class 'NoneType'>":
        length = len(path)-1
        print(length)

        return length
    else:
        length = 99999999
        print(length)
        return length

def distance(x,y):
    x1 = x[0]-y[0]
    y1 = x[1]-y[1]
    return x1+y1







