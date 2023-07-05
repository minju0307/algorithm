n = int(input())
array = list(map(int, input().split()))

# DP 테이블 초기화 
d = [0] * 100

# 다이나믹 프로그래밍 (바텀업)
d[0] = array[0] # 첫 번째 식량창고를 털었을 때의 값!
d[1] = max(array[0], array[1]) # 첫번째와 두번째 중 더 양이 많은 식량창고를 털었을 때의 값
for i in range(2, n):
  d[i] = max(d[i-1], d[i-2]+array[i])

# 계산된 결과 출력
print(d[n-1])

  



