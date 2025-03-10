
import sys
input = sys.stdin.readline
N = int(input())
marking = [[False for _ in range(N)] for _ in range(N)]
maps = [list(map(int, input().split())) for _ in range(N)]
town = 0

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
        if maps[i][j] == 1 and marking[i][j] == False:
            town += 1
            dfs(i, j, town)

# 단지 수 출력
print(town)

# 각 단지내 집의 수 계산 및 출력
house_counts = [0] * (town + 1)
for i in range(N):
    for j in range(N):
        if marking[i][j] > 0:
            house_counts[marking[i][j]] += 1

# 단지내 집의 수를 오름차순으로 정렬하여 출력
house_counts = sorted(house_counts[1:])
for count in house_counts:
    print(count)
