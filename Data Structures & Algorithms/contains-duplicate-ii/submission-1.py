class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash = set()
        L = 0 

        for R in range(len(nums)):
            if R-L > k : 
                hash.remove(nums[L])
                L+=1
            if nums[R] in hash:
                return True 
            hash.add(nums[R])
        return False 
        