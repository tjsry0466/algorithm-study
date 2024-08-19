from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums) -> int:
        dp = []

        for i in nums:
            k = bisect_left(dp, i) #자신이 들어갈 위치 k
            if len(dp) <= k: #i가 가장 큰 숫자라면
                dp.append(i)
            else:
                dp[k] = i #자신보다 큰 수 중 최솟값과 대체
        return len(dp)

