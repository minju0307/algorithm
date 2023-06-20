from collections import deque

n, m = map(int, input().split())

graph=[]
for i in range(n):
  graph.append(list(map(int, input())))


# 이동할 4가지 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue=deque()
  queue.append((x,y))

  while queue:
    x, y =queue.popleft()

    # 4방향 모두 탐색
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      ## 미로 맵을 벗어나는 경우 그 쪽으로는 못 가는 것!
      if nx <0 or ny<0 or nx>=n or ny>=m:
        continue

      ## 괴물이 있는 경우 그 쪽으로는 못 가는 것!
      if graph[nx][ny] == 0:
        continue

      ## 갈 수 있는 경우, 해당 노드를 처음 방문할 때 (즉 graph[nx][ny]==1 일 때만) 
      ## 최단거리로 경로 더해주기 
      if graph[nx][ny] == 1 : # 처음 방문하는 것을 보장 (값이 1) 
        if not (nx == 0 and ny == 0) :
          graph[nx][ny] = graph[x][y] + 1
          queue.append((nx, ny))

  return graph[n-1][m-1] # 가장 오른쪽 아래까지의 최단 거리 반환 


print(bfs(0,0))


# 입력 예시
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111