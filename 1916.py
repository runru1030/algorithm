# N개의 도시가 있다. 그리고 한 도시에서 출발하여 다른 도시에 도착하는 M개의 버스가 있다. 우리는 A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 한다. A번째 도시에서 B번째 도시까지 가는데 드는 최소비용을 출력하여라. 도시의 번호는 1부터 N까지이다.


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