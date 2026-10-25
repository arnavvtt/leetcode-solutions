class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        i=0
        bestending=nums[0]
        ans=nums[0]
        for i in range (1,len(nums)):
            i1=bestending+nums[i]
            i2=nums[i]
            bestending=max(i1,i2)
            ans=max(ans,bestending)
        return ans
        