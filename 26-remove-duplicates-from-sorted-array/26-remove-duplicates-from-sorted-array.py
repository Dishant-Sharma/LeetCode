class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums)==1:
            return 1
        
        left_pointer,right_pointer=0,0
        
        while right_pointer<len(nums):
            if right_pointer>0 and nums[right_pointer]==nums[right_pointer-1]:
                right_pointer+=1
            else:
                nums[left_pointer]=nums[right_pointer]
                left_pointer+=1
                right_pointer+=1
        return left_pointer