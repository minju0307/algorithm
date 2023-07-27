N = int(input())

students = []
for _ in range(N):
  name, korean, english, math = input().split()
  students.append((name, int(korean), int(english), int(math)))
'''
따로따로 하고 싶으면, 후순위부터 정렬을 해줘야 함
# 이름이 사전순으로 증가하는 순서로 
students = sorted(students, key = lambda x : x[0])

# 수학 점수가 감소하는 순서로 
students = sorted(students, key = lambda x : x[3], reverse=True)

# 영어 점수가 증가하는 순서로 
students = sorted(students, key = lambda x : x[2])

# 국어 점수가 감소하는 순서로 
students = sorted(students, key = lambda x : x[1], reverse=True)
'''

# -를 활용하면 reverse를 다양하게 사용할 수 있음
# lambda를 통해서 우선순위별로 정렬할 수 있음
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name, _, _, _ in students:
  print(name)
