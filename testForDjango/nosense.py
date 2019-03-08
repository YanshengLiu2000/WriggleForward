# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return '<{}>'.format(self.val)

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        self.res = False
        if not pRoot2:
            return False
        self.inOrder(pRoot1, pRoot2)
        return self.res

    def inOrder(self, node1, node2):
        if self.res:
            return
        if not node1:
            return
        self.inOrder(node1.left, node2)
        if node1.val == node2.val:
            # self.res = self.Match(node1, node2)
            if self.Match(node1,node2):#这里不可以每次循环都改动!
                self.res=True
        self.inOrder(node1.right, node2)

    def Match(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 and node2:
            return False
        if node1 and not node2:
            return True
        if node1.val == node2.val:
            return self.Match(node1.left, node2.left) and self.Match(node1.right, node2.right)
        else:
            return False

def printTree(node):
    def _Depth(node):
        if not node:
            return 0
        depth=max(_Depth(node.left),_Depth(node.right))+1
        return depth

    depth=_Depth(node)
    stack=[node]
    while stack:
        level=stack[:]
        stack=[]
        while level:
            node=level.pop(0)
            if depth>0:
                for _ in range(2**(depth)-1):
                    print(' ',end='')
            if node:
                print(node.val, end='')
                stack.append(node.left)
                stack.append(node.right)
            else:
                print('#',end='')
        depth-=1
        print()

def buildTree(treeList):
    res=[TreeNode(None) for _ in treeList]
    for i in range(len(res)):
        if treeList[i]=='#':
            res[i]=None
        else:
            res[i].val=treeList[i]
    index=-1
    while index < len(treeList):
        index += 1
        try:
            res[index].left = res[2 * index + 1]
        except:
            pass
        try:
            res[index].right = res[2 * index + 2]
        except:
            pass
    return res[0]

def Deserialize(s):

    if not s:
        return None
    res = [TreeNode(0) for i in s]
    for i in range(len(s)):
        if s[i] != '#':
            res[i].val = s[i]
        else:
            res[i] = None
    index = -1
    while index < len(s):
        index += 1
        try:
            res[index].left = res[2 * index + 1]
        except:
            pass
        try:
            res[index].right = res[2 * index + 2]
        except:
            pass

    return res[0]

def Serialize(root):
    # write code here
    if not root:
        return '#'
    stack = [root]
    res = []
    while stack:
        level = stack[:]
        stack = []
        while level:
            node = level.pop(0)
            if node:
                res.append(node.val)
                if not node.left and not node.right:
                    continue
                stack.append(node.left)
                stack.append(node.right)
            else:
                res.append('#')
    return res
t1=[5,4,'#',3,'#',2]
t2=[8,9,2]
testTree=[10,20,30,4,'#','#',5,6,'#','#','#','#','#',7,'#']
testhead=buildTree(testTree)
printTree(testhead)
print('res=',Serialize(testhead))
print('real=',testTree)