'''
给定一个二维平面，平面上有 n 个点，求最多有多少个点在同一条直线上。

【思路】
y=kx+by=kx+b 确定一条直线，获得两点之间的斜率和截距就可以得到一条线
计算每两个点练成的线，用字典储存，key为斜率和截距，value为这条线上的点
'''
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 将点按照从小到大排序 方便计算斜率
        points.sort(key=lambda x: x[0])
        points.sort(key=lambda x: x[1])
        
        if len(points)<3 : return len(points)
        '''
		由于当数值特别大时，精度计算会出问题，故使用最简分数形式表达，即分子分母除以最大公约数
		'''
        def gcd(x,y): # 最大公约数函数
            if y==0:
                return x
            else:
                return gcd(y,x%y)
           
        def linear(a,b): # 计算斜率和截距
            if a[0]==b[0]: return a[0]
            y,x=a[1]-b[1],a[0]-b[0]
            k=y/x
            b=a[1]-k*a[0]
            g=gcd(x,y)
            if g!=0:
                k='{},{}'.format(y//g,x//g)
            else:
                k='{},{}'.format(y,x)

            return ','.join([str(k),str(b)])

        from collections import defaultdict
        dic=defaultdict(list)
        for i in range(len(points)-1):
            for j in range(i+1,len(points)):                    
                if points[i] not in dic[linear(points[j],points[i])]:
                    dic[linear(points[j],points[i])].append(points[i])
                if points[j] not in dic[linear(points[j],points[i])]:
                    dic[linear(points[j],points[i])].append(points[j])
        # 由于存在重复点，对点进行计数
        return max([sum([points.count(i) for i in v]) for v in dic.values()])
