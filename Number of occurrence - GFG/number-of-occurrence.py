#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
		firstPosition=self.findFirstPosition(arr,x)
		
		if firstPosition ==-1: # no occurrence
		    return 0
		lastPosition=self.findLastPosition(arr,x)
		
		return lastPosition-firstPosition+1

    def findFirstPosition(self,nums,target):
        ansIndex=-1
        start=0
        end=len(nums)-1

        while start<=end:
            mid=start+ (end-start)//2

            # comparison and decision
            if nums[mid]==target:
                ansIndex=mid
                end=mid-1 # continue binary search in left part
            # decision
            elif nums[mid]>target:
                end=mid-1
            
            else:
                start=mid+1

        return ansIndex 

    def findLastPosition(self,nums,target):
        ansIndex=-1
        start=0
        end=len(nums)-1

        while start<=end:
            mid=start+(end-start)//2

            # comparison and decision
            if nums[mid]==target:
                ansIndex=mid
                start=mid+1 # continue binary search in right part
            # decision
            elif nums[mid]>target:
                end=mid-1
            
            else:
                start=mid+1

        return ansIndex 
#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends