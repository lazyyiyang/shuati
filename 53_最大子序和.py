# 53 最大子序和
'''
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
'''
# 复杂度O(N)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i]=nums[i]+max(nums[i-1],0) # 状态转移公式
        return max(nums)