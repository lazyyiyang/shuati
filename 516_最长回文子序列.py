'''
>给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。
示例 1:
输入:
"bbbab"
输出:
4

【思路】
```python3
if s[i]==s[j]:
	dp[i][j]= dp[i+1][j-1]+2
else: 
	dp[i][j]=max(dp[i][j-1],dp[i+1][j])
```
输出状态：返回dp[0][-1] (整个字符串)
具体实现：
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for _ in range(n)] # dp状态矩阵
        for i in range(n): # 任何数自己就是回文
            dp[i][i]=1
        for i in range(n,-1,-1): # 从右下角开始
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j]=2+dp[i+1][j-1]
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][-1] # 返回右上角



