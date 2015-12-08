# coding=utf-8
'''
拓扑排序
http://songlee24.github.io/2015/05/07/topological-sorting/
http://gracece.com/2014/04/some-small-algorithm/
下面程序 为Leetcode 210题 https://leetcode.com/problems/course-schedule-ii/
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def findOrder(self, numCourses, neighbor):
        map = [[] for x in range(numCourses)]      # 与该节点连通的其他节点
        indegree = [0 for x in range(numCourses)]  # 节点的入度
        res = []
        for p in neighbor:
            if p[0] not in map[p[1]]:
                indegree[p[0]] += 1
                map[p[1]].append(p[0])
        st = []
        for i in range(numCourses):
            if indegree[i] == 0:
                st.append(i)
        count = 0
        while st:
            tmp = st.pop(0)
            res.append(tmp)
            count += 1           # 统计入度为0的节点的个数
            for i in map[tmp]:   # 将与此入度为零的节点相连的其他节点断开
                indegree[i] -= 1
                if indegree[i] == 0:
                    st.append(i)

        if count < numCourses:   # 若图中仍存在入度不为零的节点，证明图中有环！
            return []
        else:                    # 若此时图中的节点入度均为零
            return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
#
if __name__ == "__main__":

    result = Solution().canFinish(3,[[0,2],[2,1],[1,0]])
    print(result)

