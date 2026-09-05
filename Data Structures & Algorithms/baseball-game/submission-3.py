class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []

        for ops in operations:
            if ops.lstrip('-').isdigit():
                result.append(int(ops))
            
            elif (ops == '+' ):
                new_sum = result[-2] + result[-1]
                result.append(new_sum)
            
            elif (ops == 'D'):
                
                double_sum =  2 * result[-1] 
                result.append(double_sum)

            elif(ops=='C'):
                result.pop()
        
        return sum(result)
        