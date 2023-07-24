S = input()

result=int(S[0])

for idx, number in enumerate(S[1:], start=1):
  if int(number) == 0 or int(number) == 1: ## 지금 숫자가 0이나 1
    result += int(number)
  elif int(S[idx-1]) == 0 or int(S[idx-1]) == 1: ## 이전 숫자가 0이나 1
    result += int(number)
  else:
    result *= int(number)

print(result)
