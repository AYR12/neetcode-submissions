class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        R = []
        for i in strs :
            t = "".join(sorted(i))
            seen[t].append(i)
        
        for j in seen : 
            R.append(seen[j])
        
        return R 

        
        