import sys
input = sys.stdin.readline

def solution(S):
  visited = set()
  global result
  result = ""
  def dfs(a, b, c, prev2, prev):
    global result
    
    if a + b + c == 0:
      return True
      
    if c > 0 and prev != "C" and prev2 != "C":
      key = f"{a},{b},{c-1},{prev},C"
      if key not in visited:
        result += "C"
        if dfs(a, b, c-1, prev, "C"):
          return True
        result = result[:-1]
        visited.add(key)
    if b > 0 and prev != "B":
      key = f"{a},{b-1},{c},{prev},B"
      if key not in visited:
        result += "B"
        if dfs(a, b-1, c, prev, "B"):
          return True
        result = result[:-1]
        visited.add(key)
    if a > 0:
      key = f"{a-1},{b},{c},{prev},A"
      if key not in visited:
        result += "A"
        if dfs(a-1, b, c, prev, "A"):
          return True
        result = result[:-1]
        visited.add(key)
        
  a, b, c = S.count("A"), S.count("B"), S.count("C")
  
  if dfs(a, b, c, "", "") :
    return result
  return -1
  
S = input()
print(solution(S))

# 스타트링크에는 세명의 직원이 일을 하고 있다. 세 직원의 이름은 강호(A), 준규(B), 수빈(C) 이다.

# 이 회사의 직원은 특별한 룰을 가지고 있는데, 바로 하루에 한 명만 출근한다는 것이다. 3일간의 출근 기록이 "AAC"라는 것은 처음 이틀은 A가 출근했고, 셋째 날엔 C만 출근했다는 뜻이다.

# A는 매일 매일 출근할 수 있다. B는 출근한 다음날은 반드시 쉬어야 한다. C는 출근한 다음날과 다다음날을 반드시 쉬어야 한다. 따라서, 모든 출근 기록이 올바른 것은 아니다. 예를 들어, B는 출근한 다음날 쉬어야 하기 때문에, "BB"는 절대로 나올 수 없는 출근 기록이다. 

# 출근 기록 S가 주어졌을 때, S의 모든 순열 중에서 올바른 출근 기록인 것 아무거나 출력하는 프로그램을 작성하시오.