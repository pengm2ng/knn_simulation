from resources import frontier_function, map
from resources.agent import Agent

agent_list = []
init_pos = frontier_function.initialize_agent_position(map.map_data1, map.explored_data, 6)

for ag in range(6):

    agent = Agent(init_pos[ag][0], init_pos[ag][1], [])
    agent_list.append(agent)

print(agent_list[1].x)