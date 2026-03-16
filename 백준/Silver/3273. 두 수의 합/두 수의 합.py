n = int(input())
A = list(map(int, input().split()))
x = int(input())
A.sort()
count = 0
left = 0
right = n - 1

while left < right:
    if A[left] + A[right] == x:
        count += 1
        left += 1
        right -= 1
    elif A[left] + A[right] < x:
        left += 1
    else:
        right -= 1

print(count)
