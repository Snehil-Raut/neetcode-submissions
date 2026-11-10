class Solution:
    def calPoints(self, operations: List[str]) -> int:
        results = []

        for i in range(len(operations)):

            positive = (operations[i].lstrip('-'))
            if positive.isdigit():
                results.append(int(operations[i]))
                
            elif (operations[i] == '+'):
                add = int(results[-1]) + int(results[-2])
                
                results.append(add)

            elif(operations[i] == 'D'):
                
                double = int(results[-1]) * 2
                results.append(double)

            elif (operations[i] == 'C'):
                results.pop()
        
        return sum(results)
