#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        maxSum = float("-inf")
        curSum = 0

        for i,val in enumerate(nums):
            if val < val + curSum:
                curSum += val
                nums[i] = curSum
            else:
                curSum = val
                
            if maxSum < curSum:
                maxSum = curSum

        return maxSum













        # if len(nums) == 1:
        #     return nums[0]
        # post = nums[:]
        # pre = nums[:]

        # n = len(nums)

        # for i in range(1, n):
        #     pre[i] += pre[i-1]
        # for i in range(n-2,-1,-1):
        #     post[i] += post[i+1]

        # preMaxi = 0
        # postMaxi = n-1
        # for i in range(1,n):
        #     if pre[preMaxi] < pre[i]:
        #         preMaxi = i
        #     if post[postMaxi] < post[n-i-1]:
        #         postMaxi = n-1-i 
        # if preMaxi == len(nums)-1:
        #     preMaxi -=1
        # print(f"pre:{pre}\npost:{post}\nsubArr:{preMaxi},{postMaxi}")
        # res = sum(nums[postMaxi:preMaxi+1])

        # return res
       
        

        # if len(nums) == 1:
        #     return nums[0]
        # res = float("-inf")
        # for i in range(len(nums)):
        #     cur = 0
        #     for num in nums[i:]:
        #         cur += num
        #         res = max(cur,res)
        # return res
# @lc code=end

