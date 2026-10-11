class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for s in matrix: 
            if s[-1]< target: 
                continue
            else: 
                for i in s: 
                    if i == target: 
                        return True 
        return False 
        