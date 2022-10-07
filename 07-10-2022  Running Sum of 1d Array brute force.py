class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cummulative_sum = 0 #cummulative sum
        for i in range(len(nums)):
            cummulative_sum += nums[i]
            nums[i] = cummulative_sum
        return nums