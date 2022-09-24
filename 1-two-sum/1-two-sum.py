class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            key_complement=target-nums[i]
            if key_complement in dict:
                return (i,dict[key_complement])
            
            dict[nums[i]]=i
                
        