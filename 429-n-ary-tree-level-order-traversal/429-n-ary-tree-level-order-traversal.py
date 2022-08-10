"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:    return []
        res = []
        tmp = deque()
        tmp.append(root)
        while tmp:
            l2 = []
            l1 = len(tmp)
            for i in range(l1):
                node = tmp.popleft()
                l2.append(node.val)
                if node.children:
                    for i in node.children:
                        tmp.append(i)
            res.append(l2)



        return(res)