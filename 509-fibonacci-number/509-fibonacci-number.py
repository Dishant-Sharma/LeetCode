class Solution:
    def fib(self, n: int) -> int:
        return self.returnsNthFiboNumber(n,{})
    
    def returnsNthFiboNumber(self,n,memo):
        
        if n==0:
            return 0
        
        if n==1:
            return 1
        
        currentKey=n
        
        if n in memo:
            return memo[n]
        
        # here x is n-1 calculation
        x=self.returnsNthFiboNumber(n-1,memo)
        
        # here y is n-2 calculation
        y=self.returnsNthFiboNumber(n-2,memo)
        
        memo[n]=x+y
        
        return memo[n]
        
        