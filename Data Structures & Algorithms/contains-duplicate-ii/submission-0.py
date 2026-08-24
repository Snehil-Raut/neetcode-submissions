class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):

                if nums[i] == nums[j]:
                    check_sum = abs(i-j)
                    if check_sum <= k:
                        return True
        
        return False



        