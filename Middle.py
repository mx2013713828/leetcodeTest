
class Node(object):
    def __init__(self,elem= -1,lchild=None,rchild = None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild
class middle(object):
    def __init__(self):
        self.root = Node()
    def front_digui(self,root):
        if root == None:
            return

        self.front_digui(root.lchild)
        print root.elem,
        self.front_digui(root.rchild)

root = Node(elem=4)
root.rchild = Node(elem=2)
root.rchild.lchild = Node(elem=3)

middle = middle()
middle.front_digui(root)