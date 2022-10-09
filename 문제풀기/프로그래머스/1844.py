import sys
from collections import deque
sys.stdin = open("_게임맵최단거리.txt")

graph = input()
visited = graph

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    queue = [(a,b)]
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(graph[0]) and 0 <= ny < len(graph):
                visited[nx][ny]