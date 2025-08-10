import sys
input = sys.stdin.readline

def solution(N, M, mars):
  dp =[[[0, 0] for _ in range(M)] for _ in range(N)]
  MIN = -1e9
  
  for i in range(N):
    for j in range(M):
      if i == 0:
        dp[i][j][0] = mars[i][j] + (0 if j == 0 else dp[i][j-1][0])
        dp[i][j][1] = MIN
        continue

      # 오른쪽으로
      dp[i][j][0] = mars[i][j] + max(max(dp[i-1][j]), (MIN if j == 0 else dp[i][j-1][0]))
      # 왼쪽으로
      dp[i][-(j+1)][1] = mars[i][-(j+1)] + max(max(dp[i-1][-(j+1)]), (MIN if j == 0 else dp[i][-j][1]))
  return max(dp[-1][-1])
      
N, M = map(int, input().split())
mars = []
for _ in range(N):
  mars.append(list(map(int, input().split())))

print(solution(N, M, mars))

# NASA에서는 화성 탐사를 위해 화성에 무선 조종 로봇을 보냈다. 실제 화성의 모습은 굉장히 복잡하지만, 로봇의 메모리가 얼마 안 되기 때문에 지형을 N×M 배열로 단순화 하여 생각하기로 한다.

# 지형의 고저차의 특성상, 로봇은 움직일 때 배열에서 왼쪽, 오른쪽, 아래쪽으로 이동할 수 있지만, 위쪽으로는 이동할 수 없다. 또한 한 번 탐사한 지역(배열에서 하나의 칸)은 탐사하지 않기로 한다.

# 각각의 지역은 탐사 가치가 있는데, 로봇을 배열의 왼쪽 위 (1, 1)에서 출발시켜 오른쪽 아래 (N, M)으로 보내려고 한다. 이때, 위의 조건을 만족하면서, 탐사한 지역들의 가치의 합이 최대가 되도록 하는 프로그램을 작성하시오.