n = int(input())
fear = sorted(list(map(int, input().split())))
# 공포도가 낮은 팀원 순으로 정렬하여, 그 사람부터 길드를 구성하도록

result = 0  # 결성할 수 있는 최대의 그룹 수
count = 0  # 현재 그룹에 포함된 모험가의 수

for i in fear:
  count += 1  # 현재 그룹에 포함시키기
  if count >= i:  # 현재의 공포도보다 높으면
    result += 1  # 그룹 결성!
    count = 0

print(result)
