# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.
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
