INT_MAX=999999999

n, m = map(int, input().split())
money=[]
for _ in range(n):
  money.append(int(input()))
money=sorted(money)

# dp 테이블
d = [INT_MAX] * (m+1)
d[0]=0

for i in range(money[0], m+1):
  for mm in money:
    if mm > i:
      break
    d[i]=min(d[i], d[i-mm]+1)

if d[m]==INT_MAX:
  print(-1)
else:
  print(d[m])
  


    