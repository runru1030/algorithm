# 그래프의 한 정점 S에서 다른 한 정점 T로 이동하려 한다. 이동할 때 T에 가까워지며 이동하는 경우, 이를 합리적인 이동경로라 한다. 물론 이러한 경로는 최단경로가 아닐 수도 있다.

# 그래프가 주어졌을 때 가능한 합리적인 이동경로의 개수를 구하는 프로그램을 작성하시오. S = 1, T = 2 인 경우로 한다.
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

  # 각 노드에서 T와의 거리를 구함.
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
        # u보다 T와 가까은 노드만 탐색
        if dist[v] < dist[u]:
            # v에서 T까지의 이동 경로후 누적 u-(v-T)
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


