'''
Leetcode220 存在重复元素3
在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。
如果存在则返回 true，不存在返回 false。

【思路】
暴力法：两重循环O(n^2)
二分查找法：目标数字区间为v-t<=x<=v+t，因为集合为有序数组，故可以使用二分查找（有序就想到二分查找）对record进行查找，先查找大于等于下界的最小数，在判断是否小于等于上界。
'''
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        record=set() # 滑动窗口集合
        for i in range(len(nums)):
            if len(record)>0:
                r=list(record)
                idx=self.get(r,nums[i]-t) # 对集合进行二分查找，查找大于等于下界最小元素的坐标
                if idx!=-1 and r[idx]<=nums[i]+t: # 在判断是否小于等于上界
                    return True
            record.add(nums[i])
            if len(record)>k:
                record.remove(nums[i-k])
        return False
    # 二分查找函数
    def get(self,l,t):
        i,j=0,len(l)-1
        while i<j:
            mid=(j+i)//2 # 临界点
            if l[mid]<t:
                i=mid+1
            else:
                j=mid
        return i if l[i]>=t else -1 # 若集合中无目标数字，则返回-1
