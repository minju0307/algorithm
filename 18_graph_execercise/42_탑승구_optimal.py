# 서로소 집합 알고리즘으로 풀면 효율적으로 해결할 수 있다. 
# parent가 0이 되는 경우, 더이상 도킹 할 수 없는 상태로 보고 그만한다.

def find_parent(parent, x):
  # 자기 자신이 parent가 아닌 경우 parent를 재귀적으로 호출하여 찾는다.
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union (parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a<b:
    parent[b]=a
  else:
    parent[a]=b

g = int(input())
p = int(input())

parent = [i for i in range(g+1)]
planes=[]

for _ in range(p):
  planes.append(int(input()))

result = 0
for max_gate_idx in planes:
  value = find_parent(parent, max_gate_idx)
  if value == 0:
    break
  union(parent, value, value-1)
  result +=1
  print(parent)

print(result)