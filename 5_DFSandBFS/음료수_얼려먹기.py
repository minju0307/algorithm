# 그래프 세로, 가로 길이 입력받기 
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기 
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# DFS 로 특정한 노들 방문한 뒤에 연결된 모든 노드들도 방문한 것으로 처리 
## 이렇게 하면 그 다음에 함수에 들어왔을 때는 False로 잡혀서 뭉텅이들의 개수만큼만 반환할 수 있음 

def dfs(x,y):
  # 범위에 맞지 않으면 종료 
  if x<=-1 or x>=n or y<=-1 or y>=m: 
    return False 

  # 현재 노드를 아직 방문하지 않았으면 
  ## 연관된 모든 노드들 방문처리 한 다음
  ## True를 반환 

  if graph[x][y] == 0:
    graph[x][y] = 1 # 해당 노드 방문 처리 
    # 노드 옆에 있는 상하좌우를 dfs 호출 -> 그러면 모두 방문 처리 됨 
    # 사실상 여기 에서 True나 False가 반환되는 것은 전체 결과에는 의미가 없음 (반영되지 않음)
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True


# 모든 노드를 돌아가면서 dfs 호출하기 
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i,j)==True:
      result+=1

print(result)

    