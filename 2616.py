import sys
input = sys.stdin.readline

def solution(N, peoples, K):
  if N == 0 or K == 0: return 0
  dp = [[0]*N for _ in range(3)]
  
  for i in range(3):
    for j in range(i*K, N-K+1):
      if j == 0:
        dp[i][j] = sum(peoples[j:j+K])
        continue
        
      if i == 0:
        dp[i][j] = max(dp[i][j-1], sum(peoples[j:j+K]))
      else:
        dp[i][j] = max(dp[i][j-1], sum(peoples[j:j+K]) + dp[i-1][j-K])
  
  return max(dp[-1])
  
N = int(input())
peoples = list(map(int, input().split()))
K = int(input())
print(solution(N, peoples, K))

# 기관차가 고장났을 때 끌고 가던 객차 모두를 소형 기관차 3대가 나누어 끌 수 없기 때문에, 소형 기관차들이 어떤 객차들을 끌고 가는 것이 좋을까하는 문제를 고민하다가 다음과 같이 하기로 결정하였다.

# 소형 기관차가 최대로 끌 수 있는 객차의 수를 미리 정해 놓고, 그보다 많은 수의 객차를 절대로 끌게 하지 않는다. 3대의 소형 기관차가 최대로 끌 수 있는 객차의 수는 서로 같다.
# 소형 기관차 3대를 이용하여 최대한 많은 손님을 목적지까지 운송하도록 한다. 각 객차 마다 타고 있는 손님의 수는 미리 알고 있고, 다른 객차로 손님들이 이동하는 것은 허용하지 않는다.
# 각 소형 기관차는 번호가 연속적으로 이어진 객차를 끌게 한다. 객차는 기관차 바로 뒤에 있는 객차부터 시작하여 1번 부터 차례로 번호가 붙어있다.