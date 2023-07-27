from collections import deque

N = int(input())
K = int(input())

# 보드판 초기화 
board = [ [0]*N for _ in range(N)]
  
# (테두리는 -1, 뱀의 몸은 -1, 아무것도 아닌 것은 0, 사과의 위치는 1) 이 되도록

# 테두리 채우기
for row in board:
  row.insert(0, -1)
  row.insert(len(row)+1, -1)
board.insert(0, [-1]*(N+2))
board.insert(len(board)+1, [-1]*(N+2))

# 뱀의 몸은 -1
board[1][1]=-1

# 사과 위치 채우기 
for _ in range(K):
  r, c = map(int, input().split())
  board[r][c] = 1


# 방향 전환 
L = int(input())
change_time=[]
change=[]
for _ in range(L):
  t, d = input().split()
  change_time.append(int(t))
  change.append(d)

print("초기 보드")
for iii in board:
  print(iii)
print()

# 이동하는 모듈 
def move(location, direction):
  if direction == 'right':
    location[1] += 1
  elif direction == 'left':
    location[1] += -1
  elif direction == 'up':
    location[0] += -1
  elif direction == 'down':
    location[0] += 1
  return location

# 회전하는 모듈 
def change_direction(change, direction):
  directions=['right', 'down', 'left', 'up']
  directions=deque(directions)
  idx=directions.index(direction)
  if change == 'D':
    directions.rotate(-1)
    new_direction=directions[idx]
  else:
    directions.rotate(1)
    new_direction=directions[idx]
  return new_direction
  
time = 0
head = [1, 1] # 행, 열
tail = [1, 1] # 행, 열 
direction = 'right'

while True:
  time += 1
  
  # 뱀이 몸길이를 늘려 머리를 다음 칸에 위치시키기
  head = move(head, direction)

  # 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝난다. 
  if board[head[0]][head[1]] == -1:
    break
    
  # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
  if board[head[0]][head[1]] == 1:
    board[head[0]][head[1]] = -1 # 머리가 이동됨 

  # 만약 이동한 칸에 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
  elif board[head[0]][head[1]] == 0:
    board[head[0]][head[1]] = -1
    board[tail[0]][tail[1]] = 0
    tail = move(tail, direction) 

  if time in change_time:
    idx = change_time.index(time)
    direction = change_direction(change[idx], direction)

  print(time, "초 후 보드")
  for iii in board:
    print(iii)
  print(f'direction: {direction}')
  print()

print(time)
  
  

  