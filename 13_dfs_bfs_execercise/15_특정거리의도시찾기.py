# 내가 생각한 알고리즘 = 다익스트라, 그러나 시간 초과가 발생할 수 있음

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
  # 초기 시작 상태는 0으로
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)
    if dist > distance[now]:
      continue
    # 현재 노드와 연결된 것들에 대하여 확인하기
    for i in graph[now]:
      cost = dist + i[1]

      # 만약 지금의 노드를 거쳐서 가는 것이 더 빠르다면
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N + 1)]
distance = [INF] * (N + 1)

for _ in range(M):
  a, b = map(int, input().split())
  graph[a].append((b, 1))

dijkstra(X)
print(distance)

dosi = []
for idx, d in enumerate(distance):
  if d == K:
    dosi.append(idx)

if len(dosi) > 0:
  for d in dosi:
    print(d, end=" ")
else:
  print(-1)
