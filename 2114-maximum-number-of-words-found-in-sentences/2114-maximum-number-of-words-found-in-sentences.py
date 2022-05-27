class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        return max(s.count(" ") for s in sentences) + 1
        # return max(s.count(" ") for s in sentences)
        
        x=0
        for word in sentences:
            x= max(s.count(" ") +1 )
        return x
        
        
    