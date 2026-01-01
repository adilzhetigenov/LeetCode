#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        post = nums[:]
        pre = nums[:]

        n = len(nums)

        for i in range(1, n):
            pre[i] += pre[i-1]
        for i in range(n-2,-1,-1):
            post[i] += post[i+1]

        preMaxi = 0
        postMaxi = n-1
        for i in range(1,n):
            if pre[preMaxi] < pre[i]:
                preMaxi = i
            if post[postMaxi] < post[n-i-1]:
                postMaxi = n-1-i 

        print(f"pre:{pre}\npost:{post}\nsubArr:{preMaxi},{postMaxi}")
        return sum(nums[postMaxi:preMaxi+1])
        

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

