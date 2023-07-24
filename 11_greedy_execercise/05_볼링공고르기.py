from collections import defaultdict

n, m = map(int, input().split())
balls = list(map(int, input().split()))

## 무게와 상관없이 고를 수 있는 조합의 수 
comb = (n*(n-1)) / 2

## 같은 공들을 뽑을 경우의 수 

count_balls=defaultdict(int)
for b in balls:
  count_balls[b]+=1

same=0
for weight, count in count_balls.items():
  if count <= 1:
    continue
  else:
    same += (count*(count-1)) / 2

print(int(comb-same))
  