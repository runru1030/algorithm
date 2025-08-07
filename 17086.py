import sys
from collections import defaultdict
input = sys.stdin.readline

def solution(N, M, sharks, board):
  visited = [[False]*M for _ in range(N)]
  
  def bfs(sx, sy):
    queue = deque([(sx, sy, 0)])
    while queue:
      x, y, d = queue.popleft()
      for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < N and 0 <= ny < M):
          continue
        if board[nx][ny] == 0 and (not visited[nx][ny] or visited[nx][ny] > d+1):
          visited[nx][ny] = d+1
          queue.append((nx, ny, d+1))

  result = 0
  for sx, sy in sharks:
    bfs(sx, sy)
  for i in range(N):
    result = max(result, max(visited[i]))
  
  return result

N = int(input())
peaples = map(int, input().split())
visited = [False]*N
graph = defaultdict(list)
for i in range(N):
  row = list(map(int, input().split()))
  board.append(row)
  for j in range(M):
    if row[j] == 1:
      sharks.append([i, j])

print(solution(N, M, sharks, board))

