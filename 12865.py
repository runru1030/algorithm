import sys
input = sys.stdin.readline

def solution(N, K, stuffs):
  dp = [[0]*(K+1) for _ in range(N+1)]

  for n in range(1, N+1):
    for k in range(1, K+1):
      curr_w, curr_v = stuffs[n]
      if curr_w > k: 
        dp[n][k] = dp[n-1][k]
        continue
    
      # 직전 기록의 최대치 <-> 현재 물건 담고 남은 무게 중 최대치 (직전 기록) 비교
      dp[n][k] = max(dp[n-1][k], curr_v + dp[n-1][k-curr_w])


    
  return dp[N-1][K]

N, K = map(int, input().split())
stuffs=[]
for i in range(N):
  stuff = list(map(int, input().split()))
  stuffs.append(stuff)

print(solution(N, K, stuffs))

