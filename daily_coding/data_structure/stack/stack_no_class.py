if __name__ == "__main__":
    import sys
    total_command_count = int(input())
    my_stack = []
    current_command_count = 0
    while current_command_count < total_command_count:
        current_command_count += 1
        current_command = input().split(" ")
        if current_command[0] == "push":
            my_stack.push(int(current_command[1]))
        elif current_command[0] == "size":
            print(len(my_stack))
        elif current_command[0] == "empty":
            if not my_stack:
                print(1)
            else:
                print(0)
        elif current_command[0] == "pop":
            if my_stack:
                print(my_stack.pop())
            else:
                print(-1)
        elif current_command[0] == "top":
            if my_stack:
                print(my_stack[-1])
            else:
                print(-1)
