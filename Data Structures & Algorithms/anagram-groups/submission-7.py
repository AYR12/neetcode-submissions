class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        L = []
        visited = []
        def Anagrams(a,b):
            if len(a) != len(b):
                return False
            return sorted(a) == sorted(b)
        visited = len(strs)*[False]

        for i in range (len(strs)): 
            if visited[i]:
                continue 

            M=[]
            M.append(strs[i])
            visited[i] = True 
            for j in range (i+1, len(strs)):
                if not visited[j] and Anagrams(strs[i], strs[j]) == True:
                    M.append(strs[j])
                    visited[j] = True 
            L.append(M)
        return L         
        