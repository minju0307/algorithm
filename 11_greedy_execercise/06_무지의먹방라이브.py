from collections import deque

def solution(food_times, k):
    answer = 0
    queue=deque()

    # 회전 음식에 순서대로 넣기 
    for idx, f in enumerate(food_times):
      queue.append((idx,f))
  
    # 정전이 일어나기 전까지 
    while k != 0:
      idx, time = queue.popleft()
      
      # 이번 그릇은 다 먹었기 때문에 다음 그릇을 먹기 
      if time == 0:
        while time == 0:
          idx, time = queue.popleft()
          
      # 꺼낸 음식을 1초 동안 먹기 
      food_times[idx] -= 1
      
      # 먹은 음식은 다시 큐의 맨 뒤에 넣기  
      queue.append((idx, food_times[idx])) 
      
      # 음식 먹은 만큼 시간이 흘러간다!
      k -= 1


    # 정전이 끝난 후 먹을 음식을 꺼내기 
    idx, time = queue.popleft()

    # 남은 음식이 있는 거 까지 가지 
    if time == 0:
      while time == 0:
        idx, time = queue.popleft()
    
    answer=idx+1
      
    return answer


food_times=[3,1,2]
k=5
print(solution(food_times, k))