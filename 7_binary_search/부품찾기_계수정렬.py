n=int(input())
array = [0]*1000001

for i in input().split():
  array[int(i)] = 1 # 가계에 있는 전체 부품 번호를 입력받아서 기록

m=int(input())
x=list(map(int, input().split()))

for i in x:
  if array[i]==1:
    print('yes', end=" ")
  else:
    print('no', end=" ")
    