class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_nums = sorted(nums)
        current=0
        
        res = []

        while current < len(new_nums)-2:
            left = current+1
            right = len(new_nums)-1

            while left < right:
                
                if(new_nums[current] + new_nums[left] + new_nums[right] == 0):
                    res.append([new_nums[current] , new_nums[left] , new_nums[right]])
                    left+=1
                    right-=1
                    
                elif(new_nums[current] + new_nums[left] + new_nums[right] < 0):
                    
                    left+=1
                elif(new_nums[current] + new_nums[left] + new_nums[right] > 0):
                
                    right-=1
            current+=1
            
        unique_ele = [list(item) for item in { tuple(row) for row in res}]
        return (unique_ele)      