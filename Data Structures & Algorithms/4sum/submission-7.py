class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        primary = 0
        
        quad_list = []

        while primary < len(nums)-3:
            secondary = primary+1
            while secondary < len(nums)-2:
                left = secondary + 1
                right = len(nums)-1

                while left < right:
                    if(nums[primary] + nums[secondary] + nums[left] + nums[right] == target):
                        sublist = [ nums[primary] , nums[secondary] , nums[left] , nums[right] ]

                        if sublist not in quad_list:
                            quad_list.append([nums[primary] , nums[secondary] , nums[left] , nums[right] ])
                        left += 1
                        right-=1
                    
                    elif(nums[primary] + nums[secondary] + nums[left] + nums[right] > target):
                        right-=1

                    elif(nums[primary] + nums[secondary] + nums[left] + nums[right] < target):
                        left+= 1

                secondary+=1

            primary+=1
             # after secondary is exhuasted

        return quad_list
            




        