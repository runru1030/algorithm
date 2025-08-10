import sys
from collections import deque, defaultdict
input = sys.stdin.readline

def solution(S):
  queue = deque([[1, 0, 0]])
  visited = set(['1,0'])

  def append_next(next_now, next_copied, next_cnt):
    key = f'{next_now},{next_copied}'
    if key in visited: return

    visited.add(key)
    queue.append([next_now, next_copied, next_cnt])

  while queue:
    now, copied, cnt = queue.popleft()
    if now == S: return cnt

    if now != copied: #복사
      append_next(now, now, cnt+1)
    if copied != 0: #붙여넣기
      append_next(now+copied, copied, cnt+1)
    if now > 1: #삭제
      append_next(now-1, copied, cnt+1)

S = int(input())
print(solution(S))


# 영선이는 매우 기쁘기 때문에, 효빈이에게 스마일 이모티콘을 S개 보내려고 한다.

# 영선이는 이미 화면에 이모티콘 1개를 입력했다. 이제, 다음과 같은 3가지 연산만 사용해서 이모티콘을 S개 만들어 보려고 한다.

# 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장한다.
# 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기 한다.
# 화면에 있는 이모티콘 중 하나를 삭제한다.
# 모든 연산은 1초가 걸린다. 또, 클립보드에 이모티콘을 복사하면 이전에 클립보드에 있던 내용은 덮어쓰기가 된다. 클립보드가 비어있는 상태에는 붙여넣기를 할 수 없으며, 일부만 클립보드에 복사할 수는 없다. 또한, 클립보드에 있는 이모티콘 중 일부를 삭제할 수 없다. 화면에 이모티콘을 붙여넣기 하면, 클립보드에 있는 이모티콘의 개수가 화면에 추가된다.

# 영선이가 S개의 이모티콘을 화면에 만드는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.

