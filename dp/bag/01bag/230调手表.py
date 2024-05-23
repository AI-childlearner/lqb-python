# 意思就是，他可以按+1，也可以按+k.
# 看上去是多源最短路(O(n²))，实际上是单源最短路(O(nlogn))，可以优化为01背包动态规划(O(n))
n, k = map(int, input().split())
dp = list(range(0, n))  # 初始化最笨策略，也就是只按+1，
for i in range(n):  # 初始化比较笨的策略，也就是只用k，最多按i次。
    ks = i * k % n  # 也就是按k次的情况，只按i次，然后在那个点和最笨策略比较
    dp[ks] = min(dp[ks], i)  # i代表我按k，按i次按到这个地方来了，和你原本的dp[ks]按法谁要次数少一些？
for i in range(n):
    dp[i] = min(dp[i - 1] + 1, dp[i - k] + 1, dp[i])  # 本次选1，本次选k,本次啥也不干（本身只按k次或者只按1次就是最优）
print(max(dp))