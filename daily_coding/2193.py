def main(N):
    if N == 1 or N == 2:
        return 1
    dp = [1, 1, *[0 for _ in range(N-2)]]
    for i in range(2, N):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[-1]

if __name__ == "__main__":
    N = int(input())
    print(main(N))
