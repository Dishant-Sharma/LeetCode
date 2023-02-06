class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        
        start=0
        end=self.findSum(A)
        answer=-1
        if M>N:
            return answer
            
        while start<=end:
            mid=start+(end-start)//2
            if(self.isPossible(A,N,M,mid)):
                answer=mid
                end=mid-1
            else:
                start=mid+1
        return answer
        
    def findSum(self,nums):
        total=0
        for x in nums:
            total +=x
        return total
    
    def isPossible(self,pages,booksCount,studentCount,bound):
        currentSum=0
        currentStudentCount=1
        for currentBookPages in pages:
            if currentBookPages > bound:
                return False
            if currentSum + currentBookPages <= bound:
                currentSum += currentBookPages
            else:
                currentStudentCount+=1
                currentSum = currentBookPages
                
                if currentStudentCount > studentCount:
                    return False
        return True
#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends