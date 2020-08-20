'''
>给定一个无序的整数数组，找到其中最长上升子序列的长度。
>示例:
输入: [10,9,2,5,3,7,101,18]
输出: 4 
解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。

【思路】
计算由每个位置结尾的最长上升子序列，取其中最大值。
状态转移方程：dp[i] = max( dp[j] + 1*( nums[i] > nums[j] ) )
'''
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0 # 边界条件
        dp=[1]*len(nums) # 初始化dp数组状态
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]: # 计算最大的dp[j]+1
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)