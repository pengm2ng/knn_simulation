from resources import frontier_function

def init_pos_generate(map_type, explored_map, agent_num, monte_num):
    init_pos_list = []
    for i in range(monte_num):
        init_pos = frontier_function.initialize_agent_position(map_type, explored_map,agent_num)
        init_pos_list.append(init_pos)
    print(init_pos_list)
    return init_pos_list



