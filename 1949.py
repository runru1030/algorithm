import sys
from collections import defaultdict
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)
def solution(N, peoples, graph):
  visited = [False]*(N+1)
  dp = [[0, 0] for _ in range(N+1)]

  def dfs(curr):
    dp[curr][1] = peoples[curr-1]
    for next in graph[curr]:
      if visited[next]: continue
      visited[next] = True
      dfs(next)
      
      dp[curr][0] += max(dp[next])
      dp[curr][1] += dp[next][0]
    
  visited[1] = True
  dfs(1)
  return max(dp[1])

N = int(input())
peoples = list(map(int, input().split()))
graph = defaultdict(list)
for _ in range(N-1):  
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)


print(solution(N, peoples, graph))

