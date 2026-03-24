import sys
input = sys.stdin.readline

n = int(input())
A = set(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

for x in B:
    print(1 if x in A else 0)
