import sys 
from itertools import combinations
input = sys.stdin.readline

N = int(input())
def solution(N):
  if N <= 10:
    return N

  temp_result = []
  for digit in range(1, 11): #자릿수
    for comb in combinations(range(10), digit):
      cadi = ''.join(map(str, reversed(list(comb))))
      temp_result.append(int(cadi))
  if N >= len(temp_result):
    return -1
  return sorted(temp_result)[N]
  
print(solution(N))