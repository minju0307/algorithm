n, k = map(int, input().split())
array_a=sorted(list(map(int, input().split())))
array_b=sorted(list(map(int, input().split())), reverse=True)

for i in range(k): ## k번 바꿔치기 연산을 수행
  array_a[i], array_b[i]= array_b[i], array_a[i]

print(sum(array_a))
  