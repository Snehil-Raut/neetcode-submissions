class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0

        min_len = len(nums)+1
        curr_sum = 0

        while right < len(nums):

            curr_sum += nums[right]


            while curr_sum >= target:
            
                window_size = right - left + 1

                min_len = min(window_size,min_len)
                curr_sum = curr_sum - nums[left]
                left+=1
                
            
            right+=1

        if(min_len == len(nums)+1):
            return 0
        else:
            return min_len

        