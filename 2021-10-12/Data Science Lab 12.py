class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if not self.items:
            print("Stack is empty")
        return

    def push(self,item):
        self.items.insert(0,item)

    def pop(self):
        self.is_empty()
        self.items.pop(0)

    def size(self):
        self.is_empty()
        print()
        print(len(self.items))

    def peak(self):
        self.is_empty()
        return print(self.items[0])

    def push_without_using_insert(self,item):
        self.is_empty()
        temp_stack = []
        temp_stack.append(item) # Adding item on top of the stack in temp stack
        for elem in self.items: # Adding values in tempstack from main item stack
            temp_stack.append(elem)
            print(self.items[0])
        for i in range(0,len(self.items)): # Removing all values in main items stack
            self.items.pop(0)
        for elem in temp_stack: # Tempstack -> Main stack items
            self.items.append(elem)


    def print(self):
        self.is_empty()
        for element in self.items:
            print(str(element) +"-->",end='')

if __name__ == "__main__":
    a = Stack()
    a.push(2)
    a.push(4)
    a.push_without_using_insert(9)
    a.print()
    a.size()