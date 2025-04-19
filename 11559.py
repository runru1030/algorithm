import sys
from collections import deque
input = sys.stdin.readline

def solution(board):
  rotated_board = list(map(list, zip(*board)))
  def update():
    for i in range(6):
      moved = []
      for j in range(12):
        if rotated_board[i][j] != ".":
          moved.append(rotated_board[i][j])
      rotated_board[i] = ["."]*(12 - len(moved)) + moved
      
  def bfs(i, j):
    candi=[(i, j)]
    target = rotated_board[i][j]
    queue = deque([(i, j)])
    rotated_board[i][j] = "."
    while queue:
      i, j = queue.popleft()
      for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        ni, nj = i+di, j+dj
        if not (0 <= ni <6 and 0 <= nj < 12):
          continue
          
        if rotated_board[ni][nj] == target:
          rotated_board[ni][nj] = "."
          queue.append((ni, nj))
          candi.append((ni, nj))
    return candi

  result = 0
  while True:
    is_deleted = False
    for i in range(6):
      for j in range(12):
        target = rotated_board[i][j]
        if target == ".":
          continue

        candi = bfs(i, j)
        if len(candi) >= 4:
          is_deleted = True
        else:
          for _i, _j in candi:
            rotated_board[_i][_j] = target
            
    if is_deleted:
      result += 1
      update()
    else:
      break
      
  
  return result

board = [input().strip() for _ in range(12)]
print(solution(board))