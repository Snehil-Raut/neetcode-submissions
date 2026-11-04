class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        min_nums = max(nums)
        while low <= high:
            mid=(low+high)//2

            if(nums[mid]==nums[high]):
                min_nums = min(nums[mid],min_nums)
                break

            elif(nums[mid]>nums[high]):
                min_nums = min(nums[mid],min_nums)
                
                low=mid+1
                
            elif(nums[mid]<nums[high] ):
                min_nums = min(nums[mid],min_nums)
                
                high=mid-1
        return min_nums
