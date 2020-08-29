'''
>给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。
示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

【思路】
使用指针对撞，有三个数字需要记录三个坐标，最外层遍历第一个坐标 `i` ，将数列排序后即从最小的一项开始遍历，
若该项>0，则不存在三数之和为0，中间位置从 `i+1` 开始遍历，末尾位置从 `len(n)` 向前遍历，该两点形成对撞式的遍历。
防止数列中的重复元素被重复计算，若下一个点等于当前点，则跳过下一个点。
代码实现：
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 将数列排序
        res=[]
        for i in range(len(nums)-2):
            if nums[i]>0: break  # 第一个元素就大于0 则不存在三数之和为0
            if i>0 and nums[i]==nums[i-1]: continue # 跳过重复元素
            l,r=i+1,len(nums)-1 # 后两个元素遍历初始位置
            while l<r: 
                s=nums[i]+nums[l]+nums[r]
                if s==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[r]==nums[r+1]: # 跳过重复元素 且确保l<r
                        r-=1
                    while l<r and nums[l]==nums[l-1]: 
                        l+=1
                    
                if s>0:r-=1
                if s<0:l+=1
        
        return res
