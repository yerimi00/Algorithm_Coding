n = int(input())
arr = []

for i in range(n):
    arr.append(input())

for i in range(n):
    print(arr[i][0]+""+arr[i][-1])