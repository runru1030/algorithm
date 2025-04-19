import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, sharks, board):
  def find_nearst_shark(sx, sy):
    queue = deque([(sx, sy, 0)])
    visited = [[False]*M for _ in range(N)]
    while queue:
      x, y, d = queue.popleft()
      for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]:
        nx, ny = x+dx, y+dy
        if not (0 <= nx < N and 0 <= ny < M) or visited[nx][ny]:
          continue
        
        if board[nx][ny] == 1:
          return d+1

        visited[nx][ny] = True
        queue.append((nx, ny, d+1))

  result = 0
  for sx, sy in sharks:
    result = max(find_nearst_shark(sx, sy), result)
    
  return result

N, M = map(int, input().split())
sharks = []
board = []
for i in range(N):
  row = list(map(int, input().split()))
  board.append(row)
  for j in range(M):
    if row[j] == 1:
      sharks.append([i, j])

print(solution(N, M, sharks, board))

