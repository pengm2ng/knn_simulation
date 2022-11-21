from test import global_unit

def map_change():
    map = [0,0,0,0,0,1]

    global_unit.call(map)

    map =[0,0,0,1,0,0,1]

    global_unit.call(map)