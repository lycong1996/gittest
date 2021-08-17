#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        t = ""
        for i in range(len(s)):
           t = s[i] + t
        print(t)
        if t == s:
            return True
        else:
            return False
# @lc code=end

