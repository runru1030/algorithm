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
