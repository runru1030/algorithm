import sys 
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
#위상정렬 알고리즘
def solution(N, M):
  graph = defaultdict(list)
  queue = deque([])
  indegree = [0]*(N+1)
  result = []
  
  for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] +=1 
  
  for i in range(1, N+1):
    if indegree[i] == 0:
      queue.append(i)
      
  while queue:
    target = queue.popleft()
    result.append(target)
    
    for i in graph[target]:
      indegree[i] -= 1
      if indegree[i] == 0:
        queue.append(i)
  return result

print(' '.join(map(str, solution(N, M))))