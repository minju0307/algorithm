INF = int(1e9)

n = int(input())
m = int(input())

# dp 테이블 생성
distance = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신과의 거리는 0 으로 설정
for i in range(1, n+1):
  for j in range(1, n+1):
    if i == j:
      distance[i][j] = 0

# 버스 정보 (엣지 정보) 입력 받기 
for _ in range(m):
  a, b, c = map(int, input().split())
  if distance[a][b] != INF: # 버스가 여러 대 일 경우 최소 값을 넣기 
    distance[a][b] = min(distance[a][b], c)
    continue
  distance[a][b]=c

'''
print()
for i in range(1, n+1):
  for j in range(1, n+1):
    print(distance[i][j], end=' ')
  print()
print()
'''

# 플로이드 워셜 알고리즘으로 dp 테이블 업데이트 하기 
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      distance[a][b] =  min(distance[a][b], distance[a][k]+distance[k][b])

for i in range(1, n+1):
  for j in range(1, n+1):
    print(distance[i][j], end=' ')
  print()