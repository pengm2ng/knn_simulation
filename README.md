# knn 기반 frontier based 탐사 기법

## 1. advanced_knn.py


## 2. knn.py

## 
## 3. 시뮬레이션


### 검증 환경
    * map_data = 원본 map ->  50*50
    * explored_map = 여태까지 explore 된 장소와 현재 agent 위치를 표시하는 map
        - close =4
        - 센서로 탐사된 곳 open = 3
        - frontier node= 2
        - agent의 위치 = 1
        - 미탐사 구역 = 0
### 검증 요소
    - 프런티어 노드의 개수
    - iteration에 따른 탐사비율
    - 에이전트 각각의 끝나는 데까지 총 이동거리
