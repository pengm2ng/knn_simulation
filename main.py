import advanced_knn
import kimst_knn
import sibal_knn
from resources import map

map_type = map.map_data1
explored_data = map.explored_data
k_num = 5
agent_num = 3
monte_num = 3
distance_weight = 0.3
dp_weight = 1-distance_weight

# advanced_knn, kimst_knn 실행
# 결과값 출력 및 데이터 반환
#advanced_knn.simulate_advanced_knn(agent_num, map.map_data1, explored_data,k_num, monte_num , distance_weight, dp_weight)
#kimst_knn.simulate_kimst_knn(agent_num, map.map_data1, explored_data, k_num, monte_num)

sibal_knn.simulate_sibal_knn(agent_num, map.map_data1, explored_data, k_num, monte_num)

# 반환 데이터 그래프로 출력