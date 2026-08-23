class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        if len(people)==0:
            return 0
        if(len(people)==1 and people[0] > limit):
            return 0
        if(len(people)==1 and people[0] <= limit):
            return 1
        

        left=0
        right=len(people)-1
        boat_count = 0

        
        while left <= right:
            if people[right] == limit:
                boat_count += 1
                right -= 1
            
            elif(people[left] + people[right] <= limit):
                boat_count += 1
                left+=1
                right-=1

            elif(people[left] + people[right] > limit):
                boat_count += 1
                right-=1
        return boat_count

                
                

        
        