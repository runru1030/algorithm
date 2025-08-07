# N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.

# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.
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