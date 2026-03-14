n = int(input())
A = list(map(int, input().split()))
m = M = A[0]

for i in range(n):
    if m > A[i]:
        m = A[i]
    if M < A[i]:
        M = A[i]

print(m, M)