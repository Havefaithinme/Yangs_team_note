# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에 오큰수는 -1이다.

# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다.
# A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

if __name__ == "__main__":
    import sys
    N = int(sys.stdin.readline())
    sequence = sys.stdin.readline().strip().split()
    sequence = list(map(int, sequence))

    def solution(sequence, N):
        ans = [-1]*N
        stack = [0]  # stack storing index of sequence.
        for i in range(1, N):
            while stack and sequence[stack[-1]] < sequence[i]:
                ans[stack.pop()] = sequence[i]
            stack.append(i)
        return ans
    ans = solution(sequence, N)
    # ans = list(map(str, ans))
    # print(" ".join(ans))
    print(*ans)
