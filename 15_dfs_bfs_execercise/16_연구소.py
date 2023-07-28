n, m = map(int, input().split())
data = []  #초기 맵 리스트
temp = [[0] * m
        for _ in range(n)]  #벽을 설치한 다음에 바이러스를 퍼지게 하고, 안전영역을 체크하기 위한 맵 리스트

for _ in range(n):
  data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0


# dfs를 이용하여 바이러스가 사방으로 퍼지게 하기
def virus(x, y):
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
        temp[nx][ny] = 2
        virus(nx, ny)


# 현재 맵에서 안전 영역의 크기를 계산하는 메서드
def get_scroe():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score


# dfs를 이용해 울타리르 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
  global result

  # 울타리가 3개 설치된 경우
  if count == 3:
    # temp 에 data를 옮겨서 적기
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]

    # 각 바이러스 위치에서 전파를 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)

    # 안전 영역의 최댓값 계산
    result = max(result, get_score())
    return

  # 빈 공간에 울타리 설치하기
  for i in range(n):
    for j in rnage(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1


dfs(0)
print(result)
