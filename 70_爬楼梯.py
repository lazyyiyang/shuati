# 70 爬楼梯
'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
'''
# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<4:return n
        a,b=1,2
        for i in range(n-2): #状态转移方程 f(k)=f(k-1)+f(k-2)
            a,b=b,a+b
        return b