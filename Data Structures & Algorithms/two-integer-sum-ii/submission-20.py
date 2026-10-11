class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        M = []
        while l<r :
            if target < numbers[l] + numbers[r]:
                r = r-1
                l = l
            elif target > numbers[l] + numbers[r]: 
                l = l+1
                r=r
            else: 
                M.append(l+1)
                M.append(r+1)
                return M 
        