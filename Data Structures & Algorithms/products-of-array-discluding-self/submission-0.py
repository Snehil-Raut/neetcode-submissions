class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        i=0
        while i < len(nums):
            j=0
            mul_var = 1
            while j < len(nums):
                if(i==j):
                    j+=1
                else:
                    mul_var *= nums[j]
                    j += 1
            result.append(mul_var)
            i+=1
        
        return result