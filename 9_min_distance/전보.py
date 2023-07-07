import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split())
graph = [[] for i in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))


def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if dist < distance[now]:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


dijkstra(start)

city = 0
city_cost = 0
for idx, cost in enumerate(distance):
  if cost == INF:
    continue
  if idx == 0 or idx == start:
    continue
  else:
    city += 1
    city_cost = max(city_cost, cost)

print(city, city_cost)
