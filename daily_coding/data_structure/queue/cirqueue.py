class CircularQueue:
    def __init__(self, queue):
        self.size = len(queue)
        self.queue = queue
        self.front = 0
        self.rear = self.size - 1

    def enqueue(self, x):
        # check if circular queue is already full
        # increase the rear index and check if the increased rear % size == front, which means the queue is full
        if (self.rear + 1) % self.size == self.front:
            print("Circular queue is already full")
        elif self.front == -1:
            self.front = self.rear = 0
            self.queue[self.front] = x
        else:
            self.rear = (self.rear + 1) % self.size + 1
            self.queue[self.rear] = x

    def dequeue(self):
        # check if the circular queue is already empty.
        if self.front == -1:
            return "The queue is empty"
        elif self.front == self.rear:  # this means theres only one element left in the circular queue
            temp = self.queue[self.front]
            self.front = self.rear = -1  # empty queue
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
