'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
# 哈希表 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,n in enumerate(nums):
            x=target-n
            if x in hashmap:
                return [hashmap[x],i]
            hashmap[n]=i

# 首尾排序查找 时间复杂度O(nlogn)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rk=sorted(range(len(nums)),key=lambda x: nums[x])
        head=0
        tail=len(nums)-1
        while nums[rk[head]]+nums[rk[tail]]==target:
        	if nums[rk[head]]+nums[rk[tail]]>target:
        		tail-=1
        	else:
        		head+=1
        return [rk[head],rk[tail]]
