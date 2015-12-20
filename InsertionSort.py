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
三、插入排序 InsertionSort

时间复杂度： 最好O(n)  最坏O(n^2) 平均O(n^2)
辅助空间：O(1)

介绍：

插入排序的工作原理是，对于每个未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

步骤：

从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果被扫描的元素（已排序）大于新元素，将该元素后移一位
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5

'''


class Solution:
    def insert_sort(self, ary):
        n = len(ary)
        for i in range(1, n):
            if ary[i] < ary[i - 1]:
                temp = ary[i]
                index = i  # 待插入的下标
                for j in range(i - 1, -1, -1):  # 从i-1 循环到 0 (包括0)
                    if ary[j] > temp:
                        ary[j + 1] = ary[j]
                        index = j  # 记录待插入下标
                    else:
                        break
                ary[index] = temp
        return ary


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":
    result = Solution().select_sort([99, 98, 97, -100, -200, 1])
    print(result)
