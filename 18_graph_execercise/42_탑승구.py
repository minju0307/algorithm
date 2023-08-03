g = int(input())
p = int(input())

# 탑승구 리스트를 초기화 
gates=[]
for idx in range(g+1):
  gates.append([idx, -1])

# 비행기 리스트를 초기화 
planes=[]
planes.append(0)
for _ in range(p):
  planes.append(int(input()))

result = 0
# 도착하는 순서대로 비행기를 살펴보면서
for plane_idx, plane in enumerate(planes[1:], start=1): 
  flag=False
  # 가능한 비어 있는 게이트 중에서, 가장 큰 숫자의 게이트에 비행기 도킹하기  
  for tup in reversed(gates[1:(plane+1)]):  
    if tup[1] == -1:
      tup[1]=plane_idx
      result +=1
      flag = True
      break
  if not flag:
    break
  
  print(gates)

print(result)

# 그러나 이건 시간 복잡도가 높아서 정답으로 처리 되기 힘들것 -> 새로운 방식을 찾아야 한다. 
