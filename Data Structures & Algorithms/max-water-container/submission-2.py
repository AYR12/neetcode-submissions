class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R = 0,len(heights)-1
        def area(L,R):
            return (R-L)*(min(heights[L],heights[R]))
        maxArea = 0 
        while L<R: 
            maxArea = max(maxArea,area(L,R))
            if heights[L]>heights[R]:
                R -=1
            else: 
                L+=1
        return maxArea

        