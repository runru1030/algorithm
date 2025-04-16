import sys 
from collections import deque
input = sys.stdin.readline

def solution(N, M, board, coins):
  queue = deque([(*coins, 0)])
  visited_list = [(coins[0], coins[1])]
  while queue:
    (x1, y1), (x2, y2), cnt = queue.popleft()
    if cnt >= 10:
      return -1
      
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      nx1, ny1 = x1+dx, y1+dy
      nx2, ny2 = x2+dx, y2+dy
      if not (0 <= nx1 < N and 0 <= ny1 < M) and not (0 <= nx2 < N and 0 <= ny2 < M):
        continue
      if not (0 <= nx1 < N and 0 <= ny1 < M) or not (0 <= nx2 < N and 0 <= ny2 < M):
        return cnt + 1
        
      if board[nx1][ny1] == '#': nx1, ny1 = x1, y1
      if board[nx2][ny2] == '#': nx2, ny2 = x2, y2
        
      if ((nx1, ny1), (nx2, ny2)) in visited_list:
        continue
      queue.append(((nx1, ny1), (nx2, ny2), cnt+1))
      visited_list.append(((nx1, ny1), (nx2, ny2)))
      
  return -1

N, M = list(map(int, input().split()))
coins = []
board = []
for i in range(N):
  board_row = list(input().strip())
  board.append(board_row)
  if 'o' in board_row:
    for j in range(M):
      if board[i][j] == 'o':
        coins.append((i, j))
        
print(solution(N, M, board, coins))