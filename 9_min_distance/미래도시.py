import heapq
import sys
input=sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) # 노드 개수, 간선 개수 
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1)) # 모든 비용이 1이기 때문 
  graph[b].append((a, 1)) # 양방향으로 갈 수 있기 때문에 둘 다 넣어줘야 한다. 

x, k = map(int, input().split())

# 다익스트라 알고리즘
def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기 
    dist, now = heapq.heappop(q)
    
    # 현재 노드가 이미 처리된 적 있는 노드라면 무시 
    if distance[now] < dist:
      continue

    # 현재 노드와 연결된 다른 인접한 노드들을 확인
    for i in graph[now]:
      cost = dist + i[1] # 현재 노드를 거쳐서 i[0] 노드로 가는 비용 
      # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0])) # 갱신된 값은 우선순위 큐에 들어간다. 
        

# x 에서 k 로 가는 최소 비용 구하기 
dijkstra(1)
start_to_k=distance[k]

# k 에서 x 로 가는 최소 비용 구하기 
distance = [INF] * (n+1)
dijkstra(k)
k_to_x=distance[x]

final=start_to_k+k_to_x
if final == INF:
  print(-1)
else:
  print(final)

