# coding=utf-8
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


'''
选择排序：

时间复杂度： 最好O(n^2)  最坏O(n^2) 平均O(n^2)
辅助空间：O(1)

介绍：

选择排序无疑是最简单直观的排序。它的工作原理如下。

步骤：

在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
源代码：(python实现)

'''

class Solution:
    def select_sort(self, ary):
        n = len(ary)
        for i in range(0, n):
            min = i  # 最小元素下标标记
            for j in range(i + 1, n):
                if ary[j] < ary[min]:
                    min = j  # 找到最小值的下标
            ary[min], ary[i] = ary[i], ary[min]  # 交换两者
        return ary


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().select_sort([99, 98, 97, -100, -200, 1])
    print(result)
