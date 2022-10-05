class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maximum_count=0
        for i in nums:
            if i==1:
                counter+=1
            else:
                counter=0
            maximum_count=max(maximum_count,counter)
        return maximum_count
        