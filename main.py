import advanced_knn
import kimst_knn
from resources import map

map_type = map.map_data1
explored_data = map.explored_data


# advanced_knn, kimst_knn 실행
# 결과값 출력 및 데이터 반환

advanced_knn.simulate_advanced_knn(3, map.map_data1, explored_data)
kimst_knn.simulate_kimst_knn(3, map.map_data1, explored_data)

# 반환 데이터 그래프로 출력