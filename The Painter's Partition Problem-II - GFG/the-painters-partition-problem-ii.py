#User function Template for python3

class Solution:
    def minTime (self, arr, n, k):
        start=0
        end=self.findSum(arr) # to get the total sum
        answer=-1
        
        # if k>n: 
        #     return answer # this corner 
            
        while start<=end: 
            mid=start+(end-start)//2
            if(self.isPossible(arr,n,k,mid)):
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
    
    def isPossible(self,pages,booksCount,studentCount,bound): # Bound is Maxlimit
        currentSum=0
        currentStudentCount=1 # 1st painter
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


if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        k = int(str[0])
        n = int(str[1])
        arr = input().split()
        for itr in range(n):
            arr[itr] = int(arr[itr])

        ob = Solution()
        print(ob.minTime(arr,n,k))
# } Driver Code Ends