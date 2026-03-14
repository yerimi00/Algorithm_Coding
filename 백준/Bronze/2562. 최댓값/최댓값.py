A = [int(input()) for _ in range(9)]
M = A[0]
number = 1

for i in range(9):
    if M < A[i]:
        M = A[i]
        number = i + 1

print(M)
print(number)