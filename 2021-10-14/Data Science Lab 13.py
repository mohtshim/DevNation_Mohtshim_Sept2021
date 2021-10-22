class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            print("Stack is empty")
        return

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        self.is_empty()
        self.items.pop(0)

    def size(self):
        self.is_empty()
        print()
        print(len(self.items))

    def peak(self):
        self.is_empty()
        return print(self.items[0])

    def enqueue_without_using_insert(self,item):
        self.items.append(item)

    def print(self):
        self.is_empty()
        for element in self.items:
            print(str(element) +"-->",end='')

if __name__ == "__main__":
    obj = Queue()
    obj.enqueue(3)
    obj.enqueue(7)
    obj.enqueue(9)
    obj.dequeue()
    obj.print()

