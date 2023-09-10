# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 다섯 가지이다.

# push X: 정수 X를 스택에 넣는 연산이다.
# pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 스택에 들어있는 정수의 개수를 출력한다.
# empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
class MyStack:
    def __init__(self):
        self.stack = []

    # 정수 X를 스택에 넣는 연산
    def push(self, x):
        self.stack.append(x)

    # 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력. 만약 스택에 들어있는 정수가 없는 경우 -1을 출력
    def pop(self):
        if self.stack:
            print(self.stack.pop())
        else:
            print(-1)

    # 스택에 들어있는 정수의 개수를 출력
    def size(self):
        print(len(self.stack))

    # 스택이 비어있으면1, 아니면 0을 출력.
    def empty(self):
        if self.stack:
            print(0)
        else:
            print(1)

    # 스택의 가장 위에 있는 정수를 출력. 만약 들어있는 정수가 없으면 -1을 출력.
    def top(self):
        if self.stack:
            print(self.stack[-1])
        else:
            print(-1)


if __name__ == "__main__":
    import sys
    total_command_count = int(input())
    my_stack = MyStack()
    current_command_count = 0
    while current_command_count < total_command_count:
        current_command_count += 1
        current_command = input().split(" ")
        if current_command[0] == "push":
            my_stack.push(int(current_command[1]))
        elif current_command[0] == "size":
            my_stack.size()
        elif current_command[0] == "empty":
            my_stack.empty()
        elif current_command[0] == "pop":
            my_stack.pop()
        elif current_command[0] == "top":
            my_stack.top()
