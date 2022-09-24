class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(set(s)) != len(set(t)):
            return False
    
        dict={}
        
        for i in range(len(t)):
            if s[i] not in dict:
                dict[s[i]]=t[i]
            elif dict[s[i]]!= t[i]:
                return False
         
        return True   