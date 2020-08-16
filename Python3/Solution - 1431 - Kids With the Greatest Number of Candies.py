class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        Arr = []
        maximum = max(candies)
        
        for i in range(len(candies)):         
            if candies[i] + extraCandies >= maximum:
                Arr.append(True)
            else:
                Arr.append(False)
        
        return Arr