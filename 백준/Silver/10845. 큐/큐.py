import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()

for i in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if not queue else 0)
    elif cmd[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif cmd[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
