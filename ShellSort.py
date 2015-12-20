# coding=utf-8


def shell_sort(ary):
    n = len(ary)
    gap = int(round(n / 2))  # 初始步长 , 用round四舍五入取整
    while gap > 0:
        for i in range(gap, n):  # 每一列进行插入排序 , 从gap 到 n-1
            temp = ary[i]
            j = i
            while j >= gap and ary[j - gap] > temp:  # 插入排序 序号j在此列对应的上面的一个是j-gap
                ary[j] = ary[j - gap]
                j -= gap
            ary[j] = temp
        gap = int(round(gap / 2))  # 重新设置步长
    return ary


res = shell_sort([2, 54, 656, 32])
print (res)
