class Solution:
    def tribonacci(self, n: int) -> int:
        return self.calculateTribo(n,{})
    
    def calculateTribo(self,n,memo):
        
        if n==0:
            return 0
        
        if n==1 or n==2:
            return 1
        
        currentIndex=n
        
        if currentIndex in memo:
            return memo[currentIndex]
        
        cal= self.calculateTribo(n-1,memo) + self.calculateTribo(n-2,memo) + self.calculateTribo(n-3,memo)
        
        memo[currentIndex]=cal
        
        return memo[currentIndex]
        