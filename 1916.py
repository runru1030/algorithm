import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
bus_map = [list(map(int, input().split())) for _ in range(M)]
S, E = list(map(int, input().split()))  
#벨만포드 알고리즘
def solution(N, M, bus_map, S, E):
  dist = [float('inf')]*(N+1)
  dist[S] = 0
  for _ in range(N):
    for a, b, c in bus_map:
      if dist[b] > dist[a]+c:
        dist[b] = dist[a]+c

  return dist[E]

print(solution(N, M, bus_map, S, E))