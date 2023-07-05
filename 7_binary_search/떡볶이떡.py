n, m = map(int, input().split())
tteok = sorted(list(map(int, input().split())))

numbers = []
for i in range(0, tteok[-1] + 1):
  numbers.append(i)


def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    hap = 0
    for t in tteok:
      if t <= mid:
        continue
      else:
        hap += (t - mid)

    if hap == target:
      return mid

    elif hap > target:
      start = mid + 1

    else:
      end = mid - 1

  return None


result = binary_search(numbers, m, 0, tteok[-1])
print(result)
