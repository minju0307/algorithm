
def binary_search(array, target, start, end):
  if start>end:
    return None
  mid= (start+end) // 2

  # 찾은 경우 중간 점 인덱스 반환
  if array[mid]==target:
    return mid

  # 중간값보다 타겟 값이 작으면 왼쪽 확인
  elif array[mid] > target:
    return binary_search(array, target, start, mid-1)

  # 중간값보다 타겟 값이 더 크면 오른쪽 확인
  else:
    return binary_search(array, target, mid+1, end)

n, target = list (map(int, input().split()))
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result=binary_search(array, target, 0, n-1)
if result==None:
  print("원소가 존재하지 않습니다.")
else:
  print(f"찾는 원소의 인덱스는 {result}")