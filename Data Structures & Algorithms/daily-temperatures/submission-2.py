class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []

        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][1]:
                stind, sttemp = stack.pop()
                days[stind] = (i - stind)
            stack.append([i,t])
        return days

