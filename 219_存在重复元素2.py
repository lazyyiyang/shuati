'''
5.1 滑动数组算法应用
Leetcode219 存在重复元素2
给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的 绝对值 至多为 k。

【思路】
使用长度为k的滑动窗口查找，若窗口内去重元素小于k，则返回true，否则继续滑动。
'''
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record=set() # 滑动窗口元素集合
        for i in range(len(nums)):
            if nums[i] in record: 
                return True
            record.add(nums[i])
            if len(record)>k: # 当集合元素超出k时，删除最左侧元素，向右滑动
                record.remove(nums[i-k])
        return False
