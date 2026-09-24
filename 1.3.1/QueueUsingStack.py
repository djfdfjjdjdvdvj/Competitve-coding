class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, x):
        self.s1.append(x)

    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow")
            return

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        print("Dequeued:", self.s2[-1])
        self.s2.pop()

    def front(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        print("Front:", self.s2[-1])

    def is_empty(self):
        return not self.s1 and not self.s2

    def display(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        for i in range(len(self.s2) - 1, -1, -1):
            print(self.s2[i], end=" ")

        for i in range(len(self.s1)):
            print(self.s1[i], end=" ")

        print()


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()
q.front()
q.dequeue()
q.display()
q.enqueue(40)
q.display()