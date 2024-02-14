import sys
input = sys.stdin.readline

n = int(input())
dp = [[0, []] for _ in range(n+1)]
dp[1][0] = 0
dp[1][1] = [1]

for i in range(2, n+1):
    dp[i][0] = dp[i-1][0] + 1
    dp[i][1] = dp[i-1][1] + [i]

    if i % 3 == 0 and dp[i][0] > dp[i // 3][0] + 1:
        dp[i][0] = dp[i // 3][0] + 1
        dp[i][1] = dp[i // 3][1] + [i]
    if i % 2 == 0 and dp[i][0] > dp[i // 2][0] + 1:
        dp[i][0] = dp[i // 2][0] + 1
        dp[i][1] = dp[i // 2][1] + [i]

print(dp[n][0])
print(*dp[n][1][::-1])


# 1 = 0
# 2 = 1
# 3 = 1
# 4 = 2
# 5 = 3
# 6 = 2
# 7 = 3
# 8 = 3
# 9 = 2
# 10 = 4