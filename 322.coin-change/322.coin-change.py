#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = amount+1
        res = [n] * n
        res[0] = 0

        for i in range(1,n):
            for c in coins:
                if i - c >= 0:
                    # print(f"{i}:{c}")
                    res[i] = min(res[i],(res[i-c]+1))
                    
        # print(res)
        
        if res[-1] > amount:
            return -1
    
        return res[-1]
        
# @lc code=end

