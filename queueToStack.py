class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.list.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        x = self.list[-1]
        self.list.pop()
        return x

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.list == []:
            return None
        else :
            return self.list[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        if len(self.list) == 0:
            return True
        else :
            return False

if __name__ == "__main__":
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.top()
    param_4 = obj.empty()
    print(param_2)
    print(param_3)
    print(param_4)