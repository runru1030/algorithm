
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

# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오