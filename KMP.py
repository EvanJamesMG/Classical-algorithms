# coding=utf-8

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
KMP 算法 （参考：http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
                http://blog.csdn.net/handsomekang/article/details/40978213
                http://www.jeepshoe.org/428644501.htm）
　移动位数 = 已匹配的字符数 - 对应的部分匹配值
 时间复杂度 O（m+n）
'''
class Solution(object):

    def kmp_match(self, s, p):
        m = len(s); n = len(p)
        cur = 0  # 起始指针cur
        while cur <= m-n:
            i = 0
            for i in range(n):
                if s[i+cur] != p[i]:
                    cur += max((i - self.pmt(p[:i])), 1) #有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                    break
            if i+1 == n and cur <= m-n: #字符完全匹配
                print(cur)
                return True
        return False

    # 部分匹配表
    def pmt(self, s):
        """
        PartialMatchTable
        """
        prefix = [s[:i+1] for i in range(len(s)-1)] #前缀
        postfix = [s[i+1:] for i in range(len(s)-1)] #后缀
        intersection = list(set(prefix) & set(postfix)) #共有元素
        if intersection:
            return len(intersection[0])  #返回共有元素的长度
        return 0



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    result = Solution().kmp_match("BBC ABCDAB ABCDABCDABDE", "BCDABCD")
    print(result)

