n=int(input())

dic={}
for i in range(n):
  name, score=input().split()
  dic[name]=score

result_dict=sorted(dic.items(), key=lambda x : x[1])

for n, s in result_dict:
  print(n, end=" ")