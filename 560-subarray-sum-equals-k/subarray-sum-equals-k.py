class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum=0
        sum=0
        count=0
        sum_count={0:1}
        for num in nums:
            current_sum+= num
            needed_sum=current_sum-k
            count+=sum_count.get(needed_sum,0)
            sum_count[current_sum]= sum_count.get(current_sum,0)+1
        return count