
# 动态规划1  斐波那契数列
# 1 1 2 3  5 8.。。
# 1.确定dp[n] dp代表斐波那契数组  dp[n]代表第n个斐波那契数列
# 2.递推公式 dp[n]=dp[n-1]+dp[n-2]
# 3.循环顺序 从前向后遍历
# 4.初始化dp数组 dp[0]=1 dp[1]=1
import numpy as np


def get_fibocna(n=10):
    dp=[0]*(n+1)
    dp[0],dp[1]=1,1
    i=2
    while i<=n:
        dp[i]=dp[i-1]+dp[i-2]
        i+=1
    print(dp)


# 动态规划2 爬楼梯 爬n层楼梯有多少种方法 可以一下爬 1 2 3层楼梯
#  dp[n]  dp代表爬楼梯的方式 dp[i]代表爬第i层有几种方法
# n=1 1
# n=2 2
# n=3 3
# n=4 5
# dp[i]=dp[i-1]+dp[i-2]

# 从前向后
#
def get_plt(n=10):
    dp=[0]*(n+1)
    dp[0],dp[1]=1,1
    dp[2]=2
    i=2
    while i<=n:
        dp[i]=dp[i-1]+dp[i-2]
        i+=1
    print(dp)

def get_plt_3(n):
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1
    dp[2],dp[3] = 2,4
    i = 3
    while i <= n:
        dp[i] = dp[i - 1] + dp[i - 2]+dp[i-3]
        i += 1
    print(dp)

# 动态规划3   爬楼梯的代价 cost=[10,20,30] 每次只能爬1 或2 层  只有往上爬的时候才会消耗相应的代价 计算第i层最小代价
def getmincost(n):
    cost = [10, 20, 30]
    dp=[0]*(n+1)
    for i in range(2,n+1):
        dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])
    print(dp)


# 动态规划4 给定初始位置的点去终点处的i，j有多少种不同路径 只能向下或者向右走
# dp[i,j]=dp[i-1][j]+dp[i][j-1]
# dp[0][j]=1
# dp[i][0]=1
def get_diff_lujig(m,n):
    dp_n=np.zeros((m,n)).tolist()
    for j in range(1,n):
        dp_n[0][j] = 1
        for i in range(1,m):
            dp_n[i][0]=1
            dp_n[i][j] = dp_n[i - 1][j] + dp_n[i][j - 1]
    print(dp_n)





if __name__ == '__main__':
    get_diff_lujig(4,3)

    zz=[[0]*5]*3
    print(zz)


