# class MinStack:
#
#     def __init__(self):
#         """
#         initialize your data structure here.
#         """
#         self.stack = []
#
#     def push(self, x: int) -> None:
#         self.stack.append(x)
#
#     def pop(self) -> None:
#         self.stack.pop()
#
#     def top(self) -> int:
#         return self.stack[-1]
#
#     def getMin(self) -> int:
#         min = self.stack[0]
#         for num in self.stack:
#             if num <= min:
#                 min = num
#         return min

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = None

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min == None or self.min > x:
            self.min = x

    def pop(self) -> None:
        tmp = self.top()
        self.stack.pop()
        if len(self.stack) == 0:
            self.min = None
            return None
        if tmp == self.min:
            self.min = min(self.stack)


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())