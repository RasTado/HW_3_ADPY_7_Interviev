class Stack:
    def __init__(self):
        self.st_list = []

    def isEmpty(self) -> bool:
        if self.st_list:
            return False
        else:
            return True

    def push(self, newel) -> None:
        self.st_list.append(newel)

    def pop(self):
        if self.st_list:
            return self.st_list.pop()

    def peek(self):
        if self.st_list:
            return self.st_list[-1]

    def size(self):
        return len(self.st_list)


if __name__ == '__main__':
    StackTest = Stack()
    StackTest.push(1)
    StackTest.push(2)
    StackTest.push(3)
    print(StackTest.isEmpty())
    print(StackTest.pop())
    print(StackTest.size())
