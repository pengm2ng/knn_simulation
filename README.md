# knn 기반 frontier based 탐사 기법


## 1. KNN-flow 
### 1-1. frontier base로 frontier point 선정함.
    * frontier point 찾는 함수 (3개의 agent를 기준으로 검색)
### 1-2. KNN 
#### if iteration == 1
    입력값은 agent의 좌표와 대조되는 입력값은 새롭게 찾아진 frontier point 들이다.
#### else
    입력값은 agent의 좌표와 agent들이 지나온 passnode 대조되는 입력값은 새롭게 찾아진 
    frontier point 들이다.
### 1-3. Adaptive KNN
- k값은 몇으로 할것인가?
- 찾아진 frontier point들을 대상으로 
    


## 2. 필요 기능


### 2-1. agent 객체 생성
    * get_position - 현재 agent의 x,y 값 불러오기.
    * get_passnode - 자신이 지나왔던 node 들의 집합 불러오기.
    * set_passnode - 현재 자신의 x,y 값을 past node 집합에 추가.
    * set_position - 현재 x,y 값 갱신하기


### 2-2. Frontier based 탐사 기능
    * get_new_frontier_node - 각각의 agent에 대하여 새로운 frontier node 발생
        input = explored_map - 여태까지 찾아진 장소와 현재 agent의 위치를 표시하는 map

### 2-3. KNN 기반 알고리즘
    * get_next_node - knn에 이전 passnode, 현재 position으로 분류하여 새로운 frontier node가 어디에 적절할지 결정
    * 결정 후 set_explored_map 실행

### 2-4 main
    *set_explored_map 
        - 자신의 위치를 1로 저장 후 이전 위치는 2로 변경
        - 센서로 탐사된곳  3 or 4으로 변경 - 현재 cell 기준 8방위 모두 3 or 4으로 변경
        - agent 1, agent 2, agent 3이 차례로 수행 


## 3. 시뮬레이션 환경


### 전역변수
    * map_data = 원본 map ->  40*40
    * explored_map = 여태까지 explore 된 장소와 현재 agent 위치를 표시하는 map
        - close =4
        - 센서로 탐사된 곳 open = 3
        - frontier node= 2
        - agent의 위치 = 1
        - 미탐사 구역 = 0