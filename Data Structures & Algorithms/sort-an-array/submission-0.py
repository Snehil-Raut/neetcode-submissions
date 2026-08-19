class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(left,right):
            new=[]  # new list to hold sorted eles
            i=0
            j=0

            # loop till either of len finishes first
            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    new.append(left[i])
                    i+=1
                else:
                    new.append(right[j])
                    j+=1

            new.extend(left[i:])
            new.extend(right[j:])

            return new
            
        if len(nums) == 1 or len(nums)==0:
            return nums
        
        # get the mid first to divide
        mid = len(nums) // 2  # floor value
        left_side = nums[:mid]
        right_side = nums[mid:]

        # again call the function to break the array till single elements
        left_side = self.sortArray(left_side)
        right_side = self.sortArray(right_side)

        return merge(left_side, right_side)



        