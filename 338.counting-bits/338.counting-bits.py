#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, n: int) -> List[int]:
        # border = 2
        # curNumOfOnes = 0
        # for i in range(1,n+1):
        #     curNumOfOnes+=1
        #     if curNumOfOnes == border:
        #         curNumOfOnes = 1
        #         border +=1    
        #     print(f"{i}:{border}")
        #     res.append(curNumOfOnes)
        res = [0]*(n+1)

        nextChange = 1
        for i in range(1,n+1):

            if i == nextChange*2:
                
                nextChange=i

            curNumOfOnes = 1 + res[i-nextChange]
            res[i]=curNumOfOnes

        return res
# @lc code=end

