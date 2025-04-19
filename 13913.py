import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solution(N, K):
  if N == K:
    print(0)
    print(N)
    return
    
  queue = deque([(N)])
  dist=[[i ,1e9] for i in range(100001)] # from, min_dist
  dist[N][1]=0
  
  while queue:
    curr = queue.popleft()
    if curr == K:
      break
      
    for next in [curr-1, curr+1, 2*curr]:
      if not 0 <= next <= 100000:
        continue

      cost = dist[curr][1]
      if dist[next][1] > cost+1:
        dist[next] = [curr, cost+1]
        queue.append(next)

  def dfs(pos, history):
    history.append(pos)
    if pos != dist[pos][0]:
      res = dfs(dist[pos][0], history)
      return res
    else:
      return history
      
  print(dist[K][1])
  result = 
  for _ in range()
    pathdist[pos][0]
  for h in reversed(dfs(K, [])):
    print(h, end=" ")
    
  return 

N, K = map(int, input().split())
solution(N, K)