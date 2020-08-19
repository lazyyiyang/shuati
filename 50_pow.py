'''
【思路】
子问题：x^n=(x^2)^(n/2)x
 
若 n 为奇数，x^n=x*x^(n−1)
 
停止条件：n=0n=0 , return 1
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        if n==0: # 终止条件
            return 1
		# 分解子问题
        if n%2==1:
            return x*self.myPow(x,n-1)
        x*=x
        return self.myPow(x,n/2)