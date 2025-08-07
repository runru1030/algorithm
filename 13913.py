# 수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다. 수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다. 순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.

# 수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
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
  for h in reversed(dfs(K, [])):
    print(h, end=" ")

  return 

N, K = map(int, input().split())
solution(N, K)