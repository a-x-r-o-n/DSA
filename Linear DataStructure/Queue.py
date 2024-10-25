class Queue:

    def __init__(self) -> None:
        self.queue = []

    count = lambda self: len(self.queue)
    is_empty = lambda self: True if self.count() == 0 else False
    enqueue = lambda self,data: self.queue.append(data)
    dequeue = lambda self: print("Queue Empty!") if self.is_empty() else self.queue.pop(0)
    peek = lambda self: print("empty queue") if self.is_empty() else self.queue[0]

    def print_queue(self):
        print("HEAD",end='=> ')
        for i in self.queue:
            print(f"{i}",end=' -> ')
        print(None)

def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(f"Peek: {q.peek()}")
    q.print_queue()
    print(f"Dequeued: {q.dequeue()}")
    q.print_queue()

if __name__ == '__main__':
    main()

