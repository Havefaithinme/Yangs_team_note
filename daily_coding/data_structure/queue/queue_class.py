# 정수를 저장하는 큐를 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

# 명령은 총 여섯 가지이다.

# push X: 정수 X를 큐에 넣는 연산이다.
# pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 큐에 들어있는 정수의 개수를 출력한다.
# empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
# front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

import sys 
class Queue:
    def __init__(self):
        self.queue = []
    def push(self, x):
        self.queue.append(x)
    def pop(self):
        if self.queue:
            self.queue.pop(0)
    def size(self):
        print(len(self.queue))    
    def empty(self):
        if self.queue:
            print(0)
        else:
            print(1)
    def front(self):
        if self.queue:
            print(self.queue[0])
        else:
            print(-1)
    def back(self):
        if self.queue:
            print(self.queue[-1])
        else:
            print(-1)

if __name__ == "__main__":
    my_queue = Queue()
    N = int(sys.stdin.readline())
    for _ in range(N):
        command = list(sys.stdin.readline())
        if command[0] == "push":
            my_queue.push(int(command[1]))
        elif command[0] == "pop":
            my_queue.pop()
        elif command[0] == "size":
            my_queue.size()
        elif command[0] == "empty":
            my_queue.empty()
        elif command[0] == "front":
            my_queue.front()
        elif command[0] == "back":
            my_queue.back()
        