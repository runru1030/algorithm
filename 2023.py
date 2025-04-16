import sys 
input = sys.stdin.readline

def solution(N):
  def isPrime(num):
    for i in range(2, int(num**0.5)+1):
      if num % i == 0:
        return False
    return True
    
  def dfs(primes, length):
    if length == N:
      return primes
      
    temp_result = []
    for prime in primes:
      for p in [1, 3, 7, 9]:
        temp = int(f'{prime}{p}')
        if isPrime(temp):
          temp_result.append(temp)
          
    return dfs(temp_result, length+1)   
    
  return dfs([2, 3, 5, 7], 1)

N = int(input())
for i in solution(N):
  print(i)
