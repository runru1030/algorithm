import sys
from collections import defaultdict, deque
from heapq import heappush, heappop
input = sys.stdin.readline

INF = int(1e7)
def solution(S, T, N, M, edges):
  if N < T: return 0
  graph = defaultdict(list)
  dp = [0]*(N+1)
  dist = [INF]*(N+1)
    
  def dijkstra():
    dist[T] = 0
    queue = [(0, T)]
    while queue:
      c, u = heappop(queue)
      for v, _c in graph[u]:
        if dist[v]> c+_c:
          dist[v] = c+_c
          heappush(queue, (dist[v], v))
  
  def dfs(u):
    if dp[u]:
        return dp[u]
    if u == 2:
        return 1
    for v, c in graph[u]:
        if dist[v] < dist[u]:
            dp[u] += dfs(v)
    return dp[u]


  for a, b, c in edges:
    graph[a].append([b, c])
    graph[b].append([a, c])

  dijkstra()
  
  dfs(S)
  return dp[S]

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
print(solution(1, 2, N, M, edges))


