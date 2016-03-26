# coding=utf-8
__author__ = 'EvanJames'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


'''

大数相乘使用数组list记录数据，类似小学时做乘法计算时竖着的计算方法：

1、把数据读入数组，  并实现数组逆转。数组顺序0~n与位数个位、十位....一致

2、创建存储结果数组，长度默认为两个被乘数长度之和

3、按位相乘并存储在对应的结果数组中

5、执行进位操作，结果数组从0开始，如果大于9则进位到下一位并获取新结果

6、结果执行逆序

'''


class Solution:
    def multipy(self):

        aaa = raw_input('aaa=')
        bbb = raw_input('bbb=')

        aaa = aaa[::-1]

        bbb = bbb[::-1]
        ccc = [0 for k in range(len(aaa) + len(bbb))]
        for i in range(0, len(aaa)):
            for j in range(0, len(bbb)):
                ccc[i + j] += int(aaa[i]) * int(bbb[j])

        for m in range(0, len(ccc)):
            if (ccc[m] > 9):
                ccc[m + 1] += ccc[m] / 10
                ccc[m] = ccc[m] % 10

        ccc.reverse()
        res = ''.join(str(i) for i in ccc)
        return res


if __name__ == '__main__':
    res = Solution().multipy()
    print(res)
