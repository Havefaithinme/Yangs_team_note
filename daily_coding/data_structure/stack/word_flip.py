import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    for _ in range(N):
        chars = sys.stdin.readline().split()
        res = []
        for char in chars:
            words = ''
            char = list(char)
            while char:
                words += char.pop()
            res.append(words)
        print(' '.join(res))
