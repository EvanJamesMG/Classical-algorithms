# coding=utf-8
__author__ = 'EvanJames'
'''
堆排序就是把最大堆堆顶的最大数取出，将剩余的堆继续调整为最大堆，再次将堆顶的最大数取出，这个过程持续到剩余数只有一个时结束
排序过程如下：
1.构造最大堆：从parent(n)也就是最后一个parent节点开始，自下往上依次调用max_heapify进行最大堆调整
2.堆排序 ：将根节点的最大的数换到尾部 ；将尾部的节点剥离； 然后将剩余节点重新进行最大堆调整

'''

def heap_sort(ary):
    n = len(ary)
    first = int(n / 2 - 1)                  # 最后一个非叶子节点 就是最后一个parent
    for start in range(first, -1, -1):      # 构造大根堆
        max_heapify(ary, start, n - 1)
    for end in range(n - 1, 0, -1):         # 堆排，将大根堆转换成有序数组
        ary[end], ary[0] = ary[0], ary[end] # 将根节点的最大的数换到尾部
        max_heapify(ary, 0, end - 1)        # 将尾部的节点剥离 然后重新进行最大堆调整
    return ary


# 最大堆调整：将堆的末端子节点作调整，使得子节点永远小于父节点
# start为当前需要调整最大堆的位置，end为调整边界
def max_heapify(ary, start, end):
    root = start
    while True:
        child = root * 2 + 1        # 调整节点的子节点
        if child > end: break
        if child + 1 <= end and ary[child] < ary[child + 1]:
            child = child + 1       # 取较大的子节点
        if ary[root] < ary[child]:  # 较大的子节点成为父节点
            ary[root], ary[child] = ary[child], ary[root]  # 交换
            root = child            #由于一次调整后，堆仍然违反堆性质，接续从子节点开始调整，使得整个堆都满足堆性质
        else:
            break
