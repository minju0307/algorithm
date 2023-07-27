N = int(input())
cards=[]
for _ in range(N):
  cards.append(int(input()))
cards.sort(reverse=True)

results=0
k =1
for number in cards:
  results += number * k
  k+=1

results -= cards[-1]

print(results)