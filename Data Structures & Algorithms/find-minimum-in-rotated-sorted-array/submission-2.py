class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        right=len(nums) - 1

        while low < right:
            mid = (low+right)//2
            if(nums[mid] < nums[right]):
                right=mid
            else:
                low=mid+1
        return nums[low]
        
        