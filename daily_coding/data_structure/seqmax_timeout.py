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
        ans = []
        for _ in range(N):
            cur_num = sequence.pop(0)
            if not sequence:  # last element
                ans.append(-1)
                return ans
            else:  # if not last element, look ahead for bigger element than current number
                before = len(ans)
                for num in sequence:
                    if num > cur_num:  # if bigger element is found
                        ans.append(num)  # append it
                        # print(ans)
                        break  # and break the loop
                    # if the loop was not broken, it means there was no number bigger than the current number
                after = len(ans)
                if before == after:
                    ans.append(-1)
            # print(ans)
    ans = solution(sequence, N)
    ans = list(map(str, ans))
    print(" ".join(ans))
