class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # 3 pointer Dutch national flag approach
        low,mid=0,0
        high=len(nums)-1
        
        def swap(i,j):
            nums[i],nums[j]=nums[j],nums[i]
        
        while mid<=high:
            if nums[mid]==0:
                swap(low,mid)
                low+=1
                mid+=1
            elif nums[mid] == 1:
                mid+=1
            else :
                swap(mid,high)
                high-=1
        return nums
                
        
        
        