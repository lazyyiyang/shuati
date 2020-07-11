# 20.有效的括号
'''
示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
'''
# 栈 时间复杂度O(n) 空间复杂度O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        dic={'(':')','{':'}','[':']'}
        tmp=[]
        for i in s:
            if i not in dic:
                if len(tmp)==0 or i!=tmp[-1]:
                     return False
                elif i==tmp[-1]:tmp.pop()
            else:
                tmp.append(dic.get(i))
        return True if not tmp else False

# 巧解
class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''