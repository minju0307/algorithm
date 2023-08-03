from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

def count_number (array, value):
  right_index = bisect_right(array, value) # 배열 안에 찾는 값이 없으면 가장 마지막 인덱스 값을 반환
  left_index = bisect_left(array, value) 
  result = right_index - left_index # 배열 안에 찾는 값이 없으면 가장 마지막 인덱스 값을 반환 
  if result > 0:
    return result
  return -1

print(count_number(array, x))