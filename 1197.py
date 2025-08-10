# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.
import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(E)]
#프림 알고리즘
def solution(V, E, graph):
  result = 0
  graph.sort(key=lambda x: x[2])
  parent = [i for i in range(V+1)]

  def find_p(a):
    if parent[a] != a:
      parent[a] = find_p(parent[a])
    return parent[a]
  def union_p(a, b):
    a = find_p(a)
    b = find_p(b)
    if a < b:
      parent[b] = a
    else:
      parent[a] = b

  for a, b, c in graph:
    if find_p(a) != find_p(b):
      union_p(a, b)
      result += c

  return result
print(solution(V, E, graph))