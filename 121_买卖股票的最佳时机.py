# 121 买卖股票的最佳时机
'''
输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
'''
# 动态规划 #重点求出状态转移方程
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2: return 0
        win=max(0,prices[1]-prices[0])
        low=min(prices[0],prices[1])
        for i in range(2,len(prices)):  #状态转移方程 f(n)=max(f(n-1),n-min(D(n-1)))
            low=min(low,prices[i])      # 第n天的最大收益=max(第n-1天最大收益 , 第n天价格减去之前的最低价格)
            win=max(win,prices[i]-low)
        return win