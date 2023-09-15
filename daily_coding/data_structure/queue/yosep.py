if __name__ == "__main__":
    import sys
    N, K = map(int, sys.stdin.readline().split())
    circle = [i+1 for i in range(N)]
    ans = "<"
    current_idx = 0
    for _ in range(N):
        current_idx = (current_idx + K - 1) % len(circle)
        ans += f"{circle.pop(current_idx)}, "
    ans = ans.rstrip(", ")
    ans += ">"
    print(ans)
