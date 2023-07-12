from collections import deque
import copy

v = int(input())
graph = [[] for i in range(v+1)] # 그래프 연결리스트
time= [0] * (v+1) # 각 강의 시간
indegree=[0] * (v+1) # 모든 노드에 대한 진입 차수 


# 방향 그래프의 모든 간선 정보 입력받기 
for i in range(1, v+1):
  data = list(map(int, input().split()))
  time[i] = data[0] # 강의 시간
  for x in data[1:-1]:
    indegree[i] +=1 # 각 노드의 진입차수 올라가고
    graph[x].append(i) # x->i 로의 노드 연결 
    
# 위상 정렬 함수 
def topology_sort():
  result=copy.deepcopy(time) # 알고리즘 수행 결과를 담을 리스트
  q = deque()
  
  # 처음에는 indegree가 0인 것들을 다 큐 안에 집어넣기 
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)

  # 큐가 비어 있지 않은 동안
  while q:
    now = q.popleft()

    for i in graph[now]:
      # 현재까지의 i를 듣는 최장 시간과 선수과목+지금과목수업 듣는 시간 중 max를 선택
      result[i] = max(result[i], result[now]+time[i])
      # 현재 노드가 가리키는 노드들의 진입차수 빼주기
      indegree[i]-=1
      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if indegree[i] == 0:
        q.append(i)

  # 위상 정렬을 수행한 결과 출력
  for i in range(1, v+1):
    print(result[i])

topology_sort()
      
    
    
    
      