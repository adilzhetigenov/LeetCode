#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        # border = 2
        # curNumOfOnes = 0
        # for i in range(1,n+1):
        #     curNumOfOnes+=1
        #     if curNumOfOnes == border:
        #         curNumOfOnes = 1
        #         border +=1 
        #     print(f"{i}:{border}")
        #     res.append(curNumOfOnes)

        powCnt = 0
        nextChange = 2
        for i in range(1,n+1):

            if i == nextChange:
                powCnt+=1
                nextChange*=2

            curNumOfOnes = 1 + res[i-2**powCnt]
            res.append(curNumOfOnes)

        return res
# @lc code=end

