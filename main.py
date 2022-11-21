import advanced_knn
import kimst_knn
import sibal_knn
import sibal_knn_no_dp
import sibal_knn_no_re
import sibural_knn
import advance_knn_real
from resources import map, init_pos, init_pos_generator
import dp_first
import dynamic_vornoi_partition_no_re
import sibal_knn_no_re_dist

map_type = map.map_data1
explored_data = map.explored_data
k_num = 1
agent_num = 3
monte_num = 1
dpw = 0.4
euw = 1-dpw

start_engine = 2




init_pos = init_pos_generator.init_pos_generate(map_type,explored_data,agent_num,monte_num)
#nit_pos = [[(10, 1), (10, 2), (10, 3), (9, 4)]]
#init_pos = [[(10, 10), (10, 11), (10, 12)]]
#kimst_knn.simulate_kimst_knn(agent_num, map_type, explored_data, 1, monte_num, init_pos)


# advanced_knn, kimst_knn 실행
# 결과값 출력 및 데이터 반환

#sibal_knn.simulate_sibal_knn(agent_num, map_type, explored_data, 5, monte_num, init_pos)
#sibal_knn_no_dp.simulate_sibal_knn(agent_num, map_type, explored_data, 5, monte_num, init_pos)

sibal_knn_no_re.simulate_sibal_knn(agent_num, map_type, explored_data, 6, monte_num, init_pos)
sibal_knn_no_re_dist.simulate_sibal_knn(agent_num, map_type, explored_data, 6, monte_num, init_pos, dpw, euw)
sibal_knn_no_re.simulate_sibal_knn(agent_num, map_type, explored_data, 7, monte_num, init_pos)
sibal_knn_no_re_dist.simulate_sibal_knn(agent_num, map_type, explored_data, 7, monte_num, init_pos, dpw, euw)
sibal_knn_no_re.simulate_sibal_knn(agent_num, map_type, explored_data, 8, monte_num, init_pos)
sibal_knn_no_re_dist.simulate_sibal_knn(agent_num, map_type, explored_data, 8, monte_num, init_pos, dpw, euw)



#dynamic_vornoi_partition_no_re.simulate_voronoi(agent_num, map_type, explored_data, 1, monte_num, init_pos)


'''
if start_engine == 0:
    sibal_knn.simulate_sibal_knn(agent_num, map.map_data1, explored_data, k_num, monte_num, init_pos)
elif start_engine == 1:
    sibural_knn.simulate_sibural_knn(agent_num, map.map_data1, explored_data, k_num, monte_num, distance_weight, dp_weight, init_pos)
elif start_engine == 2:
    kimst_knn.simulate_kimst_knn(agent_num, map.map_data1, explored_data, k_num, monte_num, init_pos)
'''
#dp_first.simulate_dp_first(agent_num, map.map_data1, explored_data, k_num, monte_num)


# 반환 데이터 그래프로 출력