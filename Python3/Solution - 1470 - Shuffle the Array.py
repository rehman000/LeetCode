class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        Arr = []
        
        for i in range(0, n):
            Arr.append(nums[i])
            Arr.append(nums[n+i])
            
        return Arr 
