import sys
input = sys.stdin.readline
H, W = map(int, input().split())
answer = 0
heights = list(map(int, input().split()))

for i in range(1, W-1):
  left = max(heights[:i])
  right = max(heights[i+1:])
  m = min(left, right)
  if m > heights[i]:
    answer += m - heights[i]
print(answer)
# 2차원 세계에 블록이 쌓여있다. 비가 오면 블록 사이에 빗물이 고인다.



# 비는 충분히 많이 온다. 고이는 빗물의 총량은 얼마일까?