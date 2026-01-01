#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        prev = 1
        cur = 2
        res = 0
        for i in range(n-2):
            res = cur + prev
            prev = cur
            cur = res
        return res




        
# @lc code=end

