class Solution:
    def climbStairs(self, n: int) -> int:
        return self.totalWaysPossible(0,n,{})
    
    def totalWaysPossible(self,cS,tS,memo):
        
        if cS==tS:
            return 1
        if cS>tS:
            return 0
        
        currentKey=cS
        
        if currentKey in memo:
            return memo[currentKey]
        
        oneJump= self.totalWaysPossible(cS+1,tS,memo)
        twoJumps= self.totalWaysPossible(cS+2,tS,memo)
        
        memo[currentKey]= oneJump+twoJumps
        return oneJump+twoJumps