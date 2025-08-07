# 남극에 사는 김지민 선생님은 학생들이 되도록이면 많은 단어를 읽을 수 있도록 하려고 한다. 그러나 지구온난화로 인해 얼음이 녹아서 곧 학교가 무너지기 때문에, 김지민은 K개의 글자를 가르칠 시간 밖에 없다. 김지민이 가르치고 난 후에는, 학생들은 그 K개의 글자로만 이루어진 단어만을 읽을 수 있다. 김지민은 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대가 되는지 고민에 빠졌다.

# 남극언어의 모든 단어는 "anta"로 시작되고, "tica"로 끝난다. 남극언어에 단어는 N개 밖에 없다고 가정한다. 학생들이 읽을 수 있는 단어의 최댓값을 구하는 프로그램을 작성하시오.
# 브루투포스 (완탐)
import sys
from itertools import combinations

input = sys.stdin.readline
N, K = map(int, input().split())
words = [set(input()[4:-5]) for _ in range(N)]
if K < 5:
  print(0)
elif K == 26:
  print(N)
else:
  answer = 0
  need = ["a", "n", "t", "i", "c"]
  marking = [0] * 26
  result = 0
  for n in need:
    marking[ord(n) - ord("a")] = 1

  def dfs(start, cnt):
    global result
    if cnt == K:
      count = 0
      for word in words:
        if all(marking[ord(w) - ord("a")] for w in word):
          count += 1
      result = max(result, count)
      return

    for i in range(start, 26):
      if marking[i] == 0:
        marking[i] = 1
        dfs(i, cnt + 1)
        marking[i] = 0
  dfs(0, 5)
  print(result)
