S = input()
result = [-1] * 26

for i in range(len(S)):
    idx = ord(S[i]) - ord('a')
    if result[idx] == -1:
        result[idx] = i

print(*result)