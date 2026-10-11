class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a = False
        count = 0 
        nums.sort()
        for i in nums:
            count+=1
            for j in nums[count:]: 
                if i == j : 
                    a = True 
        return a 
                 
            
        
        