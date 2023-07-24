## 내가 처음 해결한 방식
n = int(input())
coins = list(map(int, input().split()))
possible = []

for picking in range(1, len(coins) + 1):
  for idx, coin in enumerate(coins):
    if idx + picking >= len(coins):
      break
    hap = sum(coins[idx:idx + picking])
    possible.append(hap)

for i in range(1, 1000000):
  if i in possible:
    continue
  else:
    break

print(i)
