class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = -1
        sorted_nums = nums.sort()
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = start + (end-start) //2
            if nums[mid] != mid:
                missing = mid
                end = mid - 1
            else:
                start = mid + 1
        return len(nums) if missing == -1 else missing
        