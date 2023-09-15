class Deque:
    def __init__(self):
        self.deque = []

    def empty(self):
        if self.deque == []:
            return True
        else:
            return False

    def push_front(self, x):
        self.deque.insert(0, x)

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        if self.empty():
            return -1
        else:
            return self.deque.pop(0)

    def pop_back(self):
        if self.empty():
            return -1
        else:
            return self.deque.pop()

    def size(self):
        return len(self.deque)

    def front(self):
        if self.empty():
            return -1
        else:
            return self.deque[0]

    def back(self):
        if self.empty():
            return -1
        else:
            return self.deque[-1]


if __name__ == "__main__":
    import sys
    deque = Deque()
    N = int(sys.stdin.readline())
    for _ in range(N):
        command = sys.stdin.readline().split()
        if command[0] == "push_front":
            deque.push_front(int(command[1]))
        elif command[0] == "push_back":
            deque.push_back(int(command[1]))
        elif command[0] == "pop_front":
            print(deque.pop_front())
        elif command[0] == "pop_back":
            print(deque.pop_back())
        elif command[0] == "empty":
            if deque.empty():
                print(1)
            else:
                print(0)
        elif command[0] == "size":
            print(deque.size())
        elif command[0] == "front":
            print(deque.front())
        elif command[0] == "back":
            print(deque.back())
