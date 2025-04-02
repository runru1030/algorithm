import sys
input = sys.stdin.readline
N, S = map(int, input().split())
nums = list(map(int, input().split()))

def solution(nums, N, S):
  l, r = 0, 0
  answer = 0
  acc = nums[0]
  
    
  while r < N and l < N:
    if acc >= S:
      answer = min(answer, r-l+1) if answer != 0 else r-l+1
      if answer == 1:break
      l += 1
      acc -= nums[l-1]
    else:
      r += 1
      if r == N:break
      acc += nums[r]
      
  return answer
  
if S == 0:
  print(0)
else:
  print(solution(nums, N, S))
