#最长公共子序列 (jd2021数分笔试)
'''
输入: str1 = "abcde", str2 = "ace" 
输出: 3  
解释: 最长公共子序列是 "ace"，它的长度是 3
'''
'''
用两个指针 i 和 j 从后往前遍历 s1 和 s2，如果 s1[i]==s2[j]，那么这个字符一定在 lcs 中；
否则的话，s1[i] 和 s2[j] 这两个字符至少有一个不在 lcs 中，需要丢弃一个。

'''

def lcs(str1,str2):
	i,j=len(s1)-1,len(s2)-1
	def dp(i,j):
		if i==-1 or j==-1:
			return 0
		if s1[i]==s2[j]:
			return dp(i-1,j-1)+1
		else:
			return max(dp(i-1,j),dp(i,j-1))

	return dp(i,j)

'''
dp table:
暴力解法
'''
def lcs(str1, str2) -> int:
    m, n = len(str1), len(str2)
    # 构建 DP table 和 base case
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    # 进行状态转移
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                # 找到一个 lcs 中的字符
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
    return dp[-1][-1]




