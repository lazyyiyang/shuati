'''
>给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
>示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

【思路】
套娃问题，子串的子串回文，子串才有可能回文；
选定状态，s子串起始位置i，末尾位置j，需满足：

if s[i]==s[j]:
	if (j-1)-(i+1)<2: # 子串长度小于2 宣告回文
		dp[i][j]=True
	else:
		dp[i][j]=dp[i+1][j-1] # 子串回文 我回文
'''
# 具体实现：
class Solution:
    def longestPalindrome(self, s: str) -> str:
    	if len(s)<2: return s # 判断边界条件
        dp=[[False]*len(s) for _ in range(len(s))]  # 定义dp状态矩阵
        max_=1 # 记录回文子串长度
        start=0 # 记录子串起始位置
        for j in range(len(s)):
            for i in range(j):
                if s[i]==s[j]:
                    if j-i<3:
                        dp[i][j]=True
                    else:
                        dp[i][j]=dp[i+1][j-1]
                if dp[i][j]: # 记录最长回文子串长度以及起始位置
                    if j-i+1>max_:
                        max_=j-i+1
                        start=i
        return s[start:start+max_]
