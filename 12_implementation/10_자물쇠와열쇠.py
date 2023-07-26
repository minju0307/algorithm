# 참고: https://programming119.tistory.com/169 (스트라이드 움직이기)

from copy import deepcopy

def solution(key, lock):
    
    m = len(key)
    n = len(lock)
  
    # key를 오른쪽으로 90도씩 회전하기 
    def rotation (key):
      new_key=[]
      for j in range(m): 
        new_row=[]
        for i in range(-1, -(m+1), -1): 
          new_row.append(key[i][j])
        new_key.append(new_row)
      return new_key

    # -1로 패딩하기 
    def padding (lock):
      padding_lock=deepcopy(lock)

      # 열에서 앞뒤로 패딩하기 
      for row in padding_lock:
        for i in range(m-1):
          row.insert(0, -1)
          row.insert(len(row)+1, -1)

      # 행에서 앞뒤로 패딩하기 
      for i in range(m-1):
        padding_lock.insert(0, [-1]*(m+(m-1)*2))
        padding_lock.insert(len(padding_lock)+1, [-1]*(m+(m-1)*2))

      return padding_lock

    # 현재 craft와 key가 들어 맞는지 확인하기 
    def is_fit(lock_craft, key):
      flag = True
      for row_idx, row in enumerate(key):
        for col_idx, elm in enumerate(row):
          # 만약 -1이면 어차피 바깥의 일이므로 확인할 필요가 없음
          if lock_craft[row_idx][col_idx] == -1 :
            continue
          # 만약 1과 0 이 맞지 않는다면 (11이 충돌하거나, 00이 되면 채워지지 않은 것)
          if not (lock_craft[row_idx][col_idx] ^ elm) :
            flag = False
            break
      return flag
      
            
    # 패딩된 lock에서 m x m 을 모두 뽑아내고 그것이 fit 한지 확인 
    padding_lock=padding(lock)

    k=3 # key rotation 을 3번 해야 한다. 
    now_key=deepcopy(key)

    answer = False
    while answer == False:
      # m x m 뽑아내기 그것이 fit 하지 확인 
      for i in range(len(padding_lock)-(m-1)):
        for j in range(len(padding_lock)-(m-1)):
          lock_craft = [row[j:j+m] for row in padding_lock[i:i+m]]
          
          # 만약 자물쇠가 fit 하다면, lock의 모든 구멍이 다 채워진 것이 맞는지 확인해야 함 
          if is_fit(lock_craft, now_key):
            check_padding_lock=deepcopy(padding_lock)
            for idx, row in enumerate(check_padding_lock[i:i+m]):
              for cidx, elm in enumerate(row[j:j+m]):
                if elm == 0 and now_key[idx][cidx] == 1:
                  check_padding_lock[idx+i][cidx+j] = 1
              
            # check_padding_lock 에 0 이 하나도 없다면 answer 는 True
            count = 0
            for line in check_padding_lock:
              if 0 in line:
                break
              count +=1
              if count == len(check_padding_lock):
                answer=True
              
      k-=1
      now_key=rotation(key)

    return answer


key = [[0,0,0], [1,0,0], [0,1,1]]
lock = [[1,1,1], [1,1,0], [1,0,1]]
print(solution(key, lock))