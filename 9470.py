import sys 
from collections import defaultdict, deque
input = sys.stdin.readline

def solution(M, P, edges):
  result = 0
  graph = defaultdict(list)
  order = [[0, 0] for _ in range(M+1)]
  degree = [0]*(M+1)
  queue = deque([])
  
  for a, b in edges:
    graph[a].append(b)
    degree[b] += 1
  for di in range(1, M+1):
    if degree[di] == 0:
      queue.append(di)
      order[di] = [1, 0]

  
  while queue:
    start_node = queue.popleft()
    start_order = order[start_node][0]
    
    for end_node in graph[start_node]:
      if start_order > order[end_node][0]:
        order[end_node] = [start_order, 1]
      elif start_order == order[end_node][0]:
        order[end_node][1] += 1
        
      degree[end_node] -= 1
      if degree[end_node] == 0:
        if order[end_node][1] > 1:
          order[end_node][0] += 1
        if end_node == M: # 바다
          result = order[end_node][0]
          break
        queue.append(end_node)
      
  return result

T = int(input())
for _ in range(T):
  K, M, P = list(map(int, input().split()))
  edges = [list(map(int, input().split())) for _ in range(P)]
  print(f"{K} {solution(M, P, edges)}")