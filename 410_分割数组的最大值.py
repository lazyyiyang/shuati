'''
Leetcode410 分割数组的最大值
给定一个非负整数数组和一个整数 m，你需要将这个数组分成 m 个非空的连续子数组。设计一个算法使得这 m 个子数组各自和的最大值最小。
输入:
nums = [7,2,5,10,8]
m = 2
输出:
18
解释:
一共有四种方法将nums分割为2个子数组。
其中最好的方式是将其分为[7,2,5] 和 [10,8]，
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。

【思路】
目标值位于max(nums)和sum(nums)之间，对该区间使用二分查找；
查找条件为：子数组求和<=目标值，可以分割出的最大子集数量（可定义辅助函数表达），要求该数量=m。
'''
class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # 寻找查找目标的辅助函数
        def helper(x):
            res,tmp=0,0
            for num in nums:
                if num+tmp<=x: # 区间和不大于目标值
                    tmp+=num
                else:
                    res+=1
                    tmp=num
            return res+1
        
        i,j=max(nums),sum(nums)
        while i<j:
            mid=(i+j)//2
            if helper(mid)>m:
                i=mid+1
            else:
                j=mid
        return i  # i为满足条件的下界，即为所求最小最大值