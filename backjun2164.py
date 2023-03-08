#---자료구조 카드2 백준 2164번

# 아이디어
# 1번 부터 N번 까지 N장의 카드가 있다.
# 1번이 가장 위 N번이 가장 아래 순서로 놓여있다.
# 첫번째 가장 위 카드를 버린다.
# 두번째 가장 위 카드를 가장 아래로 옮긴다.
# 세번째 가장 위 카드를 버린다.
# 네번재 가장 위 카드를 가장 아래로 옮긴다.
# 위 내용을 카드가 한 장 남을 때 까지 반복한다.
# 남은 카드 한 장을 출력한다.
# 하나의 반복문을 사용한다.
# 반복 횟수가 홀수일 때 가장 위 카드를 버린다.
# 반복 횟수가 짝수일 때 가장 위 카드를 가장 아래로 옮긴다.
# 위 내용을 반복한다.
# 반복문의 종료조건은 카드가 한 장 남을 때이다.

# 시간복잡도
# O(N)

# 자료구조
# 카드 장 수 int N
# 카드 관리를 위한 deque queue

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
queue=deque([i for i in range(1, N+1)])

while len(queue)>1:
    queue.popleft() # 가장 위 카드 삭제    
    queue.append(queue.popleft()) # 가장 위 카드를 가장 아래로 옮긴다
print(queue[0])
