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


n, m = map(int, input().split())
parent = [0] * (n + 1)  # 0번부터 n번까지의 번호를 부여하였으므로
# 부모 테이블을 자기 자신으로 초기화
for i in range(n + 1):
  parent[i] = i

result = []
for i in range(m):
  type, a, b = map(int, input().split())
  if type == 0:  # union 연산으로 a와 b가 같은 팀이 된다
    union(parent, a, b)
  else:  # find 연산으로 a와 b가 같은 팀인지 아닌지 출력한다.
    if find_parent(parent, a) == find_parent(parent, b):
      result.append("YES")
    else:
      result.append("NO")

for r in result:
  print(r)
