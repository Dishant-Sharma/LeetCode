class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        
        for i in range(len(nums)):
            diff = total_sum - nums[i] - left_sum
            
            if diff == left_sum:
                return i
            
            left_sum += nums[i]
         
        return -1
        
        