import re

S = input()

strings=re.findall('[A-Za-z]', S)
numbers=list(map(int, re.findall('\d', S)))
strings.sort()

result=''.join(strings)+str(sum(numbers))

print(result)