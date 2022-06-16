class Solution(object):
    def sumOfUnique(self, nums):
        hashdict={}
        for i in nums:
            if i in hashdict.keys():
                hashdict[i]+=1
            else:
                hashdict[i]= 1
        sum1=0
        for key,value in hashdict.items():
            if value==1:
                sum1 +=key
        return sum1