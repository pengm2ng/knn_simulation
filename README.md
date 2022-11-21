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



### 새로운 기법
     - 기존에는 knn으로 노드를 할당하고 실제 이동거리와 dp 값이 계산되어서 결정되지만,
        다음과 같은 경우, knn 같은 경우는 실제 이동거리가 아닌 단순 직선경로로 할당되게 된다.
    - 그러므로 거리 요소를 고려하여 training set들을 새롭게 정의 하도록 해보았다.

    if training_set -> 0: [1,1], 1:[10,10] 2: [18,17]

    candidate [4,4] agent 0 과의 거리는 -> 10
    candidate [4,4] agent 1 과의 거리는 -> 6
    candidate [4,4] agent 2 과의 거리는 -> 15

    knn 으로 돌릴시 에이전트 0가 할당됨.

    미리 astar로 거리를 계산한 후 유틸리티가 높은 점들을 선정 -> 여기서 가중치를 계산한다.
    에이전트에 따른 가중치가 아닌 일반화된 가중치가 필요 -> dp 값 + 에이전트 n개 전체에 대한 거리의 합
    프런티어 후보 선정 정규화하는 과정이 필요
    
    4   4     -> 0, 0
    1   1   10 -> 10, 0
    10  10  6 -> 6, 0
    18  17  15 -> 15,0 

### 추가 기법
    만약 
    에이전트 0 12 -1
    에이전트 1 5 - 1
    일 경우 

    나머지 에이전트와 현재 프런티어 노드 와의 거리가 더 가까울 경우 해당 에이전트 stop
    만약 모두 stop일 경우