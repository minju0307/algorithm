S = input()

group_0=0
group_1=0

past = S[0]
for s in S[1:]:
  if s == past:
    past = s
    continue
  else:
    if past == '0':
      group_0 += 1
    else:
      group_1 += 1
    past = s

if S[-1] == '0':
  group_0 +=1
else:
  group_1 +=1
      
print(min(group_0,group_1))