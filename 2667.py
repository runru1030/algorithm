
import sys
input = sys.stdin.readline

N = int(input())
maps = [input().strip() for _ in range(N)]

town_marking = [[False]*N for _ in range(N)]
town = 0

def dfs(x, y, town_num):
    town_marking[x][y] = town_num
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == "1" and town_marking[nx][ny] == False:
            town_marking[nx][ny] = town_num
            dfs(nx, ny, town_num)

for i in range(N):
    for j in range(N):
        if maps[i][j] == "1" and town_marking[i][j] == False:
            town += 1
            dfs(i, j, town)
          
townCount = [0]*(town+1)
for i in range(N):
    for j in range(N):
      if not town_marking[i][j]: continue
      townCount[town_marking[i][j]] += 1

print(town)
for cnt in sorted(townCount[1:]): print(cnt)
