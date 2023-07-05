from collections import defaultdict

n = int(input())
foods = list(map(int, input().split()))

food_sort=[]
for idx, amount in enumerate(foods):
  food_sort.append((idx, amount))
food_sort.sort(key=lambda x: x[1], reverse=True) # 가장 많은 양부터 방문하고, index로 옆을 방문할 수 있는지 확인하기 위하여 

visited = [0]*(n+2) # 0 이면 방문할 수 있는 것, 1이면 방문했거나 혹은 방문할 수 없는 것, idx는 하나씩 크게 설정
result=0

for idx, amount in food_sort:
  if visited[idx+1] == 0 :
    # 그 곳간을 방문하기 
    visited[idx+1]=1
    # 인접한 곳간은 앞으로 방문할 수 없음 
    visited[idx]=1
    visited[idx+2]=1

    result+=amount


print(result)

  



