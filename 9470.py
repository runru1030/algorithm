import sys 
from collections import defaultdict, deque
input = sys.stdin.readline

def solution(M, P, edges):
  result = 0
  graph = defaultdict(list)
  order = [[0, 0] for _ in range(M+1)]
  degree = [0]*(M+1)
  queue = deque([])
  
  for a, b in edges:
    graph[a].append(b)
    degree[b] += 1
  for di in range(1, M+1):
    if degree[di] == 0:
      queue.append(di)
      order[di] = [1, 0]

  
  while queue:
    start_node = queue.popleft()
    start_order = order[start_node][0]
    
    for end_node in graph[start_node]:
      if start_order > order[end_node][0]:
        order[end_node] = [start_order, 1]
      elif start_order == order[end_node][0]:
        order[end_node][1] += 1
        
      degree[end_node] -= 1
      if degree[end_node] == 0:
        if order[end_node][1] > 1:
          order[end_node][0] += 1
        if end_node == M: # 바다
          result = order[end_node][0]
          break
        queue.append(end_node)
      
  return result

T = int(input())
for _ in range(T):
  K, M, P = list(map(int, input().split()))
  edges = [list(map(int, input().split())) for _ in range(P)]
  print(f"{K} {solution(M, P, edges)}")

# 지질학에서 하천계는 유향그래프로 나타낼 수 있다. 강은 간선으로 나타내며, 물이 흐르는 방향이 간선의 방향이 된다. 노드는 호수나 샘처럼 강이 시작하는 곳, 강이 합쳐지거나 나누어지는 곳, 바다와 만나는 곳이다.



# 네모 안의 숫자는 순서를 나타내고, 동그라미 안의 숫자는 노드 번호를 나타낸다.

# 하천계의 Strahler 순서는 다음과 같이 구할 수 있다.

# 강의 근원인 노드의 순서는 1이다.
# 나머지 노드는 그 노드로 들어오는 강의 순서 중 가장 큰 값을 i라고 했을 때, 들어오는 모든 강 중에서 Strahler 순서가 i인 강이 1개이면 순서는 i, 2개 이상이면 순서는 i+1이다.
# 하천계의 순서는 바다와 만나는 노드의 순서와 같다. 바다와 만나는 노드는 항상 1개이며, 위의 그림의 Strahler 순서는 3이다.

# 하천계의 정보가 주어졌을 때, Strahler 순서를 구하는 프로그램을 작성하시오.

# 실제 강 중에서 Strahler 순서가 가장 큰 강은 아마존 강(12)이며, 미국에서 가장 큰 값을 갖는 강은 미시시피 강(10)이다.

# 노드 M은 항상 바다와 만나는 노드이다.