class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i=0
        

        while i < len(nums):
            j=i+1
            while j < len(nums):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True
                else:
                    j+=1
        
            i+=1

        return False




        