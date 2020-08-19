'''
【题目】
给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

【思路】
子问题：对数组分为左数组与右数组

左数组众数=右数组众数，返回该众数；
若众数不同，返回在整个数组中出现更多的那个众数。
分解停止条件：区间长度=1
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        # 设置停止点
        if n==1:
            return nums[0]
        # 分解子问题
        left=self.majorityElement(nums[:n//2])
        right=self.majorityElement(nums[n//2:])
        # 治之
        if left==right:
            return left
        if nums.count(left)>nums.count(right):
            return left
        else:
            return right

