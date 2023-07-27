import heapq

# 항상 가장 작은 두 카드 묶음을 알기 위하여 우선순위 큐 구조를 사용
# heapq 라이브러리로 우선순위 큐를 사용하기

N = int(input())
heap = []
for _ in range(N):
  card = int(input())
  heapq.heappush(heap, card)

result = 0

while len(heap) != 1:
  # 가장 작은 2개의 카드 묶음 꺼내기
  one = heapq.heappop(heap)
  two = heapq.heappop(heap)
  # 카드 묶음을 합쳐서 다시 삽입
  sumvalue = one + two
  result += sumvalue
  heapq.heappush(heap, sumvalue)

print(result)
