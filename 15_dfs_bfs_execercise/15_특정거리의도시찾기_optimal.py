# 모든 간선의 비용이 1 이라는 점에서 BFS 를 통하여 최단 거리를 구할 수 있다. 
# 그러면 시간 복잡도 O(N+M) 으로 문제를 해결할 수 있다.

import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)
distance[X]=0

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append(b)

# 너비 우선 탐색 시작 
q = deque([X])
while q:
  now = q.popleft()
  # 현재 도시와 연결되어 있는 모든 도시의 거리를 탐색
  for next_node in graph[now]:
    # 아직 방문하지 않은 노드라면, 최단 거리 갱신해주기
    if distance[next_node] == INF:
      distance[next_node] = distance[now] + 1
      q.append(next_node)

dosi = []
for idx, d in enumerate(distance):
  if d == K:
    dosi.append(idx)

if len(dosi) > 0:
  for d in dosi:
    print(d, end=" ")
else:
  print(-1)