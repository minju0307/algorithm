N = input()

left=N[:(len(N)//2)]
right=N[len(N)//2:]

l_sum=0
r_sum=0

for i in left:
  l_sum += int(i)

for i in right:
  r_sum += int(i)

if l_sum == r_sum:
  print("LUCKY")
else:
  print("READY")