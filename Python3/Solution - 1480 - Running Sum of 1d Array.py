class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        Arr = []
        sum = 0
        
        for index in nums:
            sum += index
            Arr.append(sum)
        
        return Arr