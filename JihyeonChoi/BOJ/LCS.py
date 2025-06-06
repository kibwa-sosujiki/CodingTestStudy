import sys

A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

dp = [[0] * (len(B)+1) for _ in range(len(A)+1)]

for i in range(1, len(A)+1):
    for j in range(1, len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(A)][len(B)])

# | i\j  | 0 | 1(C) | 2(A) | 3(P) | 4(C) | 5(A) | 6(K) |
# | ---- | - | ---- | ---- | ---- | ---- | ---- | ---- |
# | 0    | 0 | 0    | 0    | 0    | 0    | 0    | 0    |
# | 1(A) | 0 | 0    | 1    | 1    | 1    | 1    | 1    |
# | 2(C) | 0 | 1    | 1    | 1    | 2    | 2    | 2    |
# | 3(A) | 0 | 1    | 2    | 2    | 2    | 3    | 3    |
# | 4(Y) | 0 | 1    | 2    | 2    | 2    | 3    | 3    |
# | 5(K) | 0 | 1    | 2    | 2    | 2    | 3    | 4    |
# | 6(P) | 0 | 1    | 2    | 3    | 3    | 3    | 4    |

# ACAYKP
# CAPCAK