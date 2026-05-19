def solution(sequence):
    ans = 0
    dp1, dp2 = 0, 0
    for i, v in enumerate(sequence):
        p = v if i % 2 == 0 else -v
        dp1 = max(p, dp1 + p)
        dp2 = max(-p, dp2 + (-p))
        ans = max(ans, dp1, dp2)
    return ans