class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 
        while i< len(numbers): 
            for j in range(i,len(numbers)):
                if numbers[i] == target - numbers[j]:
                    return [i+1,j+1]
            i+=1
        return False


        