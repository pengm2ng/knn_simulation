
import sibal_knn_no_re

from resources import map, init_pos, init_pos_generator

import dynamic_vornoi_partition_no_re
import sibal_knn_no_re_dist

from matplotlib import pyplot as plt


map_type = map.map_data1
explored_data = map.explored_data
k_num = 1
agent_num = 6
monte_num = 1
dpw = 0.4
euw = 1-dpw

start_engine = 2




init_pos = init_pos_generator.init_pos_generate(map_type,explored_data,agent_num,monte_num)
#nit_pos = [[(10, 1), (10, 2), (10, 3), (9, 4)]]
#init_pos = [[(10, 11), (11, 10), (11, 11)]]
#kimst_knn.simulate_kimst_knn(agent_num, map_type, explored_data, 1, monte_num, init_pos)


# advanced_knn, kimst_knn 실행
# 결과값 출력 및 데이터 반환

#sibal_knn.simulate_sibal_knn(agent_num, map_type, explored_data, 5, monte_num, init_pos)
#sibal_knn_no_dp.simulate_sibal_knn(agent_num, map_type, explored_data, 5, monte_num, init_pos)

#sibal_knn_no_re.simulate_sibal_knn(3, map_type, explored_data, 6, monte_num, init_pos)
#sibal_knn_no_re.simulate_sibal_knn(4, map_type, explored_data, 6, monte_num, init_pos)
#sibal_knn_no_re.simulate_sibal_knn(5, map_type, explored_data, 6, monte_num, init_pos)
#sibal_knn_no_re.simulate_sibal_knn(6, map_type, explored_data, 6, monte_num, init_pos)
#frontier_based.frontier_based(3, map_type, explored_data, 1, monte_num, init_pos)


result1=[]
result2=[]
result3=[]
agent_num=4
monte_num =1
for i in range(monte_num):
    #init_pos = init_pos_generator.init_pos_generate(map_type,explored_data,agent_num,1)
    init_pos = [[[2,14],[16,10],[4,6],[12,11]]]
    ret1 = sibal_knn_no_re_dist.simulate_sibal_knn(agent_num, map_type, explored_data, 6, 1, init_pos, 0.1, 0.9)
    ret3 = sibal_knn_no_re.simulate_sibal_knn(agent_num, map_type, explored_data, 6, 1, init_pos)
    ret2 = dynamic_vornoi_partition_no_re.simulate_voronoi(agent_num, map_type, explored_data, 1, 1, init_pos)

    if i == 0:
        for j in range(agent_num):
            result1.append(0)
            result2.append(0)
            result3.append(0)



    for j in range(agent_num):
        result1[j] = result1[j]+ret1[j]
        result2[j] = result2[j]+ret2[j]
        result3[j] = result3[j]+ret3[j]


for i in range(agent_num):
    result1[i] = result1[i]/monte_num
    result2[i] = result2[i]/monte_num
    result3[i] = result3[i]/monte_num

print()
print("*******************************************")
print()
print(ret1)
print("distance")
print("proposed 2: [" + str(result1)+","+str(ret1[agent_num][0])+"],")
print("voronoi : [" + str(result2)+","+ str(ret2[agent_num][0])+"],")
print("proposed 1 : ["+ str(result3)+","+ str(ret3[agent_num][0])+"],")
print()





#dynamic_vornoi_partition_no_re.simulate_voronoi(3, map_type, explored_data, 1, monte_num, init_pos)
#sibal_knn_no_re_dist.simulate_sibal_knn(4, map_type, explored_data, 6, monte_num, init_pos, dpw, euw)
#dynamic_vornoi_partition_no_re.simulate_voronoi(4, map_type, explored_data, 1, monte_num, init_pos)
#sibal_knn_no_re_dist.simulate_sibal_knn(5, map_type, explored_data, 6, monte_num, init_pos, dpw, euw)
#dynamic_vornoi_partition_no_re.simulate_voronoi(5, map_type, explored_data, 1, monte_num, init_pos)
#sibal_knn_no_re_dist.simulate_sibal_knn(6, map_type, explored_data, 6, monte_num, init_pos, dpw, euw)
#dynamic_vornoi_partition_no_re.simulate_voronoi(6, map_type, explored_data, 1, monte_num, init_pos)



#sibal_knn_no_re.simulate_sibal_knn(agent_num, map_type, explored_data, 7, monte_num, init_pos)
#sibal_knn_no_re_dist.simulate_sibal_knn(agent_num, map_type, explored_data, 7, monte_num, init_pos, dpw, euw)
#sibal_knn_no_re.simulate_sibal_knn(agent_num, map_type, explored_data, 8, monte_num, init_pos)
#sibal_knn_no_re_dist.simulate_sibal_knn(agent_num, map_type, explored_data, 8, monte_num, init_pos, dpw, euw)









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