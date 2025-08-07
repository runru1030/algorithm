# 기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다. 준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다. 그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.
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