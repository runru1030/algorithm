# 음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.
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