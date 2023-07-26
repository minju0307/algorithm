def solution(s):
    answer = len(s)
  
    # 1개 단위부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s)//2+1):
      compressed = ""
      prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출 
      count = 1 # 뭉텅이가 몇번씩 반복되었는지 확인

      # 단위 (step) 크기만큼 증가시키며 이전 문자열과 같은지 비교하기 
      for j in range(step, len(s), step):
        
        # 이전 상태와 동일하다면 압축 횟수 (count) 증가 
        if prev == s[j:j+step]:
          count+=1

        # 다른 문자열이 나왔다면 
        else:
          compressed += str(count) + prev if count>=2 else prev # 이전까지의 압축을 반영하고
          prev = s[j:j+step] # 다시 상태 초기화 
          count = 1

      # 남아있는 문자열 반영
      compressed += str(count) + prev if count >=2 else prev

      # 만들어지는 압축 문자열이 가장 짧은 것이 정답 
      answer = min(answer, len(compressed))
      
    return answer

s = "ababcdcdababcdcd"
result = solution(s)
print(result)