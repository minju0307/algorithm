N = int(input())
houses= list(map(int, input().split()))

houses.sort()
idx = (len(houses)//2) -1
print(houses[idx])