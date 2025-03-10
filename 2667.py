
import sys
input = sys.stdin.readline
N = int(input())
marking = [[False]*N for _ in range(N)]
maps = [list(map(int, input().split())) for _ in range(N)]
town = 0
print(maps)
def dfs(x, y, town_num):
    marking[x][y] = town_num
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for dx, dy in d:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and maps[nx][ny] == 1 and marking[nx][ny] == False:
            marking[nx][ny] = town_num
            dfs(nx, ny, town_num)

for i in range(N):
    for j in range(N):
        print(i, j)
        if maps[i][j] == 1 and marking[i][j] == False:
            town += 1
            dfs(i, j, town)

print(marking)