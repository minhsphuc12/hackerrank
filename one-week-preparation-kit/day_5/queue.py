class Queue:
    def __init__(self):
        self._values=[]
    
    def enqueue(self, value):
        self._values.append(value)
    
    def dequeue(self):
        self._values.pop(0)
    
    def printf(self):
        print(self._values[0])

if __name__ == '__main__':
    n_ops = int(input())
    q = Queue()
    for _ in range(n_ops):
        instruction = [int(x) for x in input().strip().split(' ')]
        operation = instruction[0]
        if operation == 1:
            q.enqueue(instruction[1])
        if operation == 2:
            q.dequeue()
        if operation == 3:
            q.printf()