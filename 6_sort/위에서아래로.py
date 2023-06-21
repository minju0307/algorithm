n = int(input())
array=[]
for i in range(n):
  array.append(int(input()))

print(sorted(array, reverse=True))