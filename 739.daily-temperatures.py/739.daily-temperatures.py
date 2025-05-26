#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# @lc code=start


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        n = len(temperatures)
        stack = deque()
        answer = [0] * n


        for i,t in enumerate(temperatures):

            while stack and temperatures[stack[-1]] < t:
                stk_i  = stack.pop()
                answer[stk_i] = i - stk_i
             #[75,71,69]
             #[1,1]   
            stack.append(i)
        

        return answer
# @lc code=end