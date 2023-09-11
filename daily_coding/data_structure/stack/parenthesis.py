import sys
if __name__ == "__main__":
    def is_valid(chars):
        my_stack = []
        for char in chars:
            if char == "(":
                my_stack.append("(")
            elif char == ")":
                if "(" in my_stack:
                    my_stack.pop()
                else:
                    return "NO"
        if my_stack:
            return "NO"
        else:
            return "YES"

    N = int(sys.stdin.readline())
    for _ in range(N):
        chars = list(sys.stdin.readline().strip())
        print(is_valid(chars))
