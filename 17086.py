import sys
from collections import deque
input = sys.stdin.readline

def solution(N, M, sharks, board):
  visited = [[False]*M for _ in range(N)]
  def find_nearst_shark(sx, sy):
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
    find_nearst_shark(sx, sy)
  for i in range(N):
    result = max(result, max(visited[i]))

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

# N×M 크기의 공간에 아기 상어 여러 마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 아기 상어가 최대 1마리 존재한다.

# 어떤 칸의 안전 거리는 그 칸과 가장 거리가 가까운 아기 상어와의 거리이다. 두 칸의 거리는 하나의 칸에서 다른 칸으로 가기 위해서 지나야 하는 칸의 수이고, 이동은 인접한 8방향(대각선 포함)이 가능하다.

# 안전 거리가 가장 큰 칸을 구해보자. 