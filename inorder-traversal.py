# -*- coding:utf-8 -*-
import collections
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#TreeNode 和Tree 都是定义树节点，可以再继续定义树类，仅仅为了演示算法，这里使用节点的关系表示一棵树即可
class Tree:
    def __init__(self,x = -1,left = None,right = None):
        self.val = x
        self.left = left
        self.right = right
#递归实现二叉树的中序遍历
class Trave:
    def __init__(self):

        self.root = Tree()
    def middle(self,root):
        if root == None:
            return
        self.middle(root.left)
        print root.val,
        self.middle(root.right)

# Morris Traversal Solution 中序遍历的一中方法 空间复杂度为1
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, curr = [], root
        while curr:
            if curr.left is None:
                result.append(curr.val)
                curr = curr.right
            else:
                node = curr.left
                #
                while node.right and node.right != curr:
                    node = node.right

                if node.right is None:
                    node.right = curr
                    curr = curr.left
                else:
                    result.append(curr.val)
                    node.right = None
                    curr = curr.right

        return result


# Time:  O(n)
# Space: O(h)
# Stack Solution  用栈实现二叉树的中序遍历
class Solution2(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result, stack = [], [(root, False)]
        while stack:
            root, is_visited = stack.pop()
            if root is None:
                continue
            if is_visited:
                result.append(root.val)
            else:
                stack.append((root.right, False))
                stack.append((root, True))
                stack.append((root.left, False))
        return result

#定义一个数据结构，双向队列~运用它实现二叉树的镜面转换
class Queue:
    def __init__(self):
        self.data = collections.deque()

    def push(self, x):
        self.data.append(x)

    def peek(self):
        return self.data[0]

    def pop(self):
        return self.data.popleft()

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0
#广度优先BFS实现树的倒置，因为没有设置树类，直接输入根节点，返回一个新的根节点，left和right改变
class Solution_invert(object):
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if root is not None:
            nodes = Queue()
            nodes.push(root)
            while not nodes.empty():
                node = nodes.pop()
                node.left, node.right = node.right, node.left
                if node.left is not None:
                    nodes.push(node.left)
                if node.right is not None:
                    nodes.push(node.right)

        return root


if __name__ == "__main__":
    root = Tree(1)
    root.right = Tree(2)
    root.right.left = Tree(3)#通过节点关系定义一棵树
    Trave = Trave()
    Trave.middle(root)
    invert = Solution_invert()
    invert.invertTree(root)
    print '\n',root.left.val,root.left.right.val
