class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.insert(0,x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        x = self.queue[-1]
        self.queue.pop()
        return x

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.queue == []:
            return None
        else :
            return self.queue[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.queue) == 0:
            return True
        else :
            return False

if __name__ == "__main__":
    obj = MyQueue()
    obj.push(2)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()