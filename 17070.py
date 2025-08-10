# https://www.acmicpc.net/problem/17070
# 파이프 옮기기1
N = int(input())
room = [0 for _ in range(N)]*N
dp = [[[0, 0, 0] for _ in range(N)] for _ in range(N)]
for r in range(N): room[r]=list(map(int, input().split(" ")))

dp[0][1][0] = 1

for i in range(2, N):
    if room[0][i] == 0:
        dp[0][i][0] = dp[0][i - 1][0]

for r in range(1,N):
  for c in range(1,N):  
    if room[r][c] == 0 and room[r][c-1] == 0 and room[r-1][c] == 0:
      dp[r][c][2] = sum(dp[r-1][c-1]) 
    if room[r][c] == 0:
      dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2] 
      dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2] 

result = sum(dp[N-1][N-1])
print(result)