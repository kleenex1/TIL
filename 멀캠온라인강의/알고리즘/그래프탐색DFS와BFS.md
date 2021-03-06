# DFS (Depth-First Search)

* DFS는 깊이 우선 탐색이라고도 부르며 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
* DFS는 스택 자료구조(혹은 재귀 함수)를 이용하며, 구체적인 동작 과정은 다음과 같다
  1. 탐색 시작 노드를 스택에 삽입하고 방문 처리를 한다
  2. 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리.
     방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복

  ![DFS](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20184242.png)
  ![DFS1](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20184304.png)
  ![DFS2](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20184331.png)
  ![DFS3](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20184346.png)
  ![DFS4](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20184403.png)
  ![DFS5](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20184431.png)

  ```python
  # DFS 메서드 정의
  def dfs(graph, v, visited):
   # 현재 노드를 방문 처리
   visited[v] = True
   print(v, end=' ')
   # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
   for i in graph[v]:
      if not visited[i]:
         dfs(graph, i, visited)

   # 실행 결과 : 1 2 7 6 8 3 4 5
  ```

  ```python
  # 각 노드가 연결된 정보를 표현 (2차원 리스트)
  graph - [
   [], # 인덱스 0은 쓰지 않도록 함
   [2, 3, 8],
   [1, 7],
   [1, 4, 5],
   [3, 5],
   [3, 4],
   [7],
   [2, 6, 8],
   [1, 7]
  ]
  # 각 노드가 방문된 정보를 표현 (1차원 리스트)
  visited = [False] * 9

  # 정의된 DFS 함수 호출
  dfs(graph, 1, visited)
  ```

# BFS (Breadth-First Search) 
(각 간선의 비용이 동일한 상황에서 최단거리 문제를 해결하기 위해 활용할 수도 있다 *자주 등장함)
* BFS는 너비 우선 탐색, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘
* BFS는 큐 자료구조를 이용
   1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
   2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
   3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
![BFS](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20190018.png)
![BFS1](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20190039.png)
![BFS2](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20190055.png)
![BFS3](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20190115.png)
![BFS4](./%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7/2022-07-17%20190131.png)

```python
from collections import deque

# BFS 메서드 정의
def bfs(graph, start, visited):
   # 큐 구현을 위해 deque 라이브러리 사용
   queue = deque([start])
   # 현재 노드를 방문 처리
   visited[start] = True
   # 큐가 빌 떄까지 반복
   while queue:
      # 큐에서 하나의 원소를 뽑아 출력하기
      v = queue.popleft()
      print(v, end=' ')
      # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
      for i in graph[v]:
         if not visited[i]:
            queue.append(i)
            visited[i] = True
```
```python
# 각 노드가 연결된 정보를 표현 (2차원 리스트)
graph = [
   [],
   [2, 3, 8],
   [1, 7],
   [1, 4, 5],
   [3, 5],
   [3, 4],
   [7],
   [2, 6, 8],
   [1, 7]
]

# 각 노드가 방문된 정보를 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)

# 결과 : 1 2 3 8 7 4 5 6
```