import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    s = input().strip()
    stack = []
    valid = True

    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if not stack:
                valid = False
                break
            else:
                stack.pop()

    if valid and not stack:
        print("YES")
    else:
        print("NO")
