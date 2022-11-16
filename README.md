# 국내 저널 

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


### kimst와 비교해 달라진 부분
    - 3,4,5 에이전트 수에 따른 비교
    - dp 개념 추가
    - 끝에서부터 5개를 training point 로 지정
 
### 비교 kimst vs advanced
    - 평균 탐사 시간
    - 평균 iteration 
    - 에이전트 각각의 평균 이동 거리

### 최상의 코드
    - [-5:] 
    agent0의 moving_distance 평균 : 45.3
    agent1의 moving_distance 평균 : 58.1
    agent2의 moving_distance 평균 : 56.5
    평균 iter : 31.9
    평균 time : 86.6

    - [-5:]x
    agent0의 moving_distance 평균 : 56.4
    agent1의 moving_distance 평균 : 56.3
    agent2의 moving_distance 평균 : 53.1   
    평균 iter : 32.0
    평균 time : 92.2

    agent0의 frontier_node 평균 : 25.1
    agent0의 moving_distance 평균 : 50.5
    agent1의 frontier_node 평균 : 25.1
    agent1의 moving_distance 평균 : 45.8
    agent2의 frontier_node 평균 : 25.1
    agent2의 moving_distance 평균 : 41.7
    agent3의 frontier_node 평균 : 25.1
    agent3의 moving_distance 평균 : 42.9
    평균 iter : 25.1
    평균 time : 88.7

    - set_explored_map
    - 거리 dp 후 knn