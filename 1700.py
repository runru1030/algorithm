import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
order = list(map(int, input().split()))
elec_item_order = defaultdict(deque)
for idx, elec_item in enumerate(order):
  elec_item_order[elec_item].append(idx)

multi_tap=[]
answer = 0
for idx, elec_item in enumerate(order):
  if elec_item not in multi_tap:
    if len(multi_tap) == N:
      multi_tap.sort(key=lambda x: elec_item_order[x][0] if elec_item_order[x] else float('inf'))
      multi_tap.pop()
      answer += 1
      
    multi_tap.append(elec_item) 
  elec_item_order[elec_item].popleft()

print(answer)