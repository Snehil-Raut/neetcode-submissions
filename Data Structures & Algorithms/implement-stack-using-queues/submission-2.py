class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []  # op queue
        

    def push(self, x: int) -> None:
        self.q1.append(x)
        
    def pop(self) -> int:
        if len(self.q1)==0:
            return 0
        else:
            s = len(self.q1)
            while s != 1:
                self.q2.append(self.q1.pop(0))
                s -= 1 
            removed = self.q1.pop(0)
            self.q1, self.q2 = self.q2, self.q1
            return removed
        

    def top(self) -> int:
        if len(self.q1)==0:
            return 0
        else:
            s = len(self.q1)
            while s != 1:
                self.q2.append(self.q1.pop(0))
                s-=1
            top =  self.q1[0]
            self.q1.pop(0)
            self.q2.append(top)
            self.q1, self.q2 = self.q2, self.q1
            return top
        

    def empty(self) -> bool:
        if len(self.q1)==0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()