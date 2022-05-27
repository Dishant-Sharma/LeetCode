class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        #return max(s.count(" ") for s in sentences) + 1
        
        
        x=0
        for s in sentences:
            x= max(x,s.count(" "))
        return x+1
    
        
            
        
        
    