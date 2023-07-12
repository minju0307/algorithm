# find 연산
def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]
  
# union 연산
def union(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# 집의 개수(node)와 길의 개수(edge) 입력받기 
n, m = map(int, input().split())

# parent table
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i

# edge table (for kruskal)
edges=[]

# edge 정보를 입력받기 
for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b)) # 비용을 넣어주기 

edges.sort()

selected_edges=[]

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b): # 사이클이 발생하지 않을 때만
    union(parent, a, b)
    selected_edges.append(edge)

selected_edges.sort(reverse=True) # 비용이 큰 순서대로!
result=0

# parent table
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i
result=0
for cost, a, b in selected_edges[1:]: 
  result+=cost

print(result)

  
    
  
  