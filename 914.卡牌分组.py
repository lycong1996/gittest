#
# @lc app=leetcode.cn id=914 lang=python3
#
# [914] 卡牌分组
#

# @lc code=start
import collections
from typing import  List


class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        count = collections.Counter(deck)
        N = len(deck)
        for i in range(2,N + 1):
            if N % i ==0:
                if all(j % i == 0 for j in count.values()):
                    return True
        return False
# @lc code=end

