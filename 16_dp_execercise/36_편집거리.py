# 참고 : https://velog.io/@dltmdrl1244/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-15483%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8E%B8%EC%A7%91-%EA%B1%B0%EB%A6%ACEdit-Distance-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98

# dp 테이블을 만들고, 세로에서 가로로 변경한다가 포인트!

a = input()
b = input()

# dp 테이블 초기화 
distance= [[0]*(len(b)+1) for _ in range(len(a)+1)]

# 각 행의 첫번째 요소를 다 채우기
for i in range(len(a)+1):
  distance[i][0]=i

# 첫 번째 열을 다 채우기 
for j in range(len(b)+1):
  distance[0][j]=j

# dp 테이블을 채워가면서 
for i in range(1, len(a)+1):
  for j in range(1, len(b)+1):
    if a[i-1] == b[j-1]: # 현재 위치의 문자열이 같은지 확인
      distance[i][j]=distance[i-1][j-1] # 대각선 방향으로 가져오기
    else:
      distance[i][j] = min (distance[i-1][j-1], distance[i-1][j], distance[i][j-1]) + 1

print(distance[len(a)][len(b)])