class MyQueue:

    def __init__(self):
        self.st1 = []
        self.st2 = []
        

    def push(self, x: int) -> None:
        self.st1.append(x)
        

    def pop(self) -> int:
        if len(self.st1) == 0 and len(self.st2) == 0:
            return 0
        else:
            s = len(self.st1)
            if len(self.st2) == 0:
                while s != 0:
                    self.st2.append(self.st1.pop())
                    s-=1
            popp = self.st2.pop(-1)
                
            return popp
        

    def peek(self) -> int:
        if len(self.st1) == 0 and len(self.st2) == 0:
            return 0
        else:
            s = len(self.st1)
            if len(self.st2) == 0:
                while s != 0:
                    self.st2.append(self.st1.pop())
                    s-=1
            top = self.st2[-1]         
            return top


    def empty(self) -> bool:
        if len(self.st1)==0 and len(self.st2)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()