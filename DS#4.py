
class Node:
    def __init__(self, newval):
        self.val = newval
        self.left = None
        self.right = None
        self.parent = None
        self.color = None
        
class RBT:
    def __init__(self):
        self.root = Node(None)
    def insert(self, tree, n):
        if self.root.val is None:
            self.root = n
            self.expand(n)
        elif n.val < tree.val:
            if tree.left.val is None:
                tree.left = n
                n.parent = tree
                self.expand(n)
            else:
                self.insert(tree.left, n)
        else:
            if tree.right.val is None:
                tree.right = n
                n.parent = tree
                self.expand(n)
            else:
                self.insert(tree.right, n)
        n.color = 'red'
        self.fixup(tree, n)
    
    def expand(self, n):
        n.left = Node(None)
        n.right = Node(None)
        n.left.parent = n
        n.right.parent = n
    
    
    def fixup(self, tree, z):
        if(z.parent is None):
            z.color = 'black'
        else:
            while(z.parent.color == 'red'):
                if(z.parent == z.parent.parent.left):
                    y = z.parent.parent.right
                    if(y.color == 'red'): # case 1
                        z.parent.color = 'black'
                        y.color = 'black'
                        z.parent.parent.color = 'red'
                        z = z.parent.parent
                        #self.print(self.root, 0)
                        #z = z.parent.parent # while 문 내에서 계속 돌아서 오류생김 z가 z.parent.parent가 됨으로 써 z.parent = None 이기 때문에 
                        #self.print(self.root, 0)
                    else:
                        if(z == z.parent.right): # case 2
                            z = z.parent
                            self.leftRotate(z)
                        z.parent.color = 'black' # case 3
                        z.parent.parent.color = 'red'
                        self.rightRotate(z.parent.parent)
                        #print("실행")
                        #self.print(self.root, 0)
                else:
                    y = z.parent.parent.left
                    if(y.color == 'red'):
                        z.parent.color = 'black'
                        y.color = 'black'
                        z.parent.parent.color = 'red'
                        z = z.parent.parent
                    else:
                        
                        if(z == z.parent.left):
                            z = z.parent
                            self.rightRotate(z)
                        z.parent.color = 'black'
                        z.parent.parent.color = 'red'
                        self.leftRotate(z.parent.parent)
                if(z.parent is None or z.parent.parent is None):
                    #self.print(self.root, 0)
                    break
            self.root.color = 'black'
            #self.print(self.root, 0)
            #print('error')

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if(y.left is not None):
            y.left.parent = x
        y.parent = x.parent
        if(x.parent is None):
            self.root = y
        elif(x is x.parent.left):
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rightRotate(self, x):
        y = x.left
        x.left = y.right
        if(y.right is not None):
            y.right.parent = x
        y.parent = x.parent
        if(x.parent is None):
            self.root = y
        elif(x is x.parent.right):
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def print(self,tree,level):
        if tree.right is not None:
            self.print(tree.right,level + 1)
        for i in range(level):
            print('   ', end='')
        print(tree.val,' , ',tree.color)
        if tree.left is not None:
            self.print(tree.left, level + 1)

    def inorder_iteration(self, tree): # inorder traversal without using recursion
        current = tree
        stack = []
        finish = False
        while(finish is not True):
            if(current is not None):
                stack.append(current)
                current = current.left
                
            else:
                if(len(stack) > 0):
                    current = stack.pop()
                    print(current.val, end=' ')
                    current = current.right

                else:
                    finish = True
    
def main():
    rbt = RBT()
    rbt.insert(rbt.root, Node(41))
    rbt.print(rbt.root, 0)
    print("\n")
    rbt.insert(rbt.root, Node(38))
    rbt.print(rbt.root, 0)
    print("\n")
    rbt.insert(rbt.root, Node(31))
    rbt.print(rbt.root, 0)
    print("\n")
    rbt.insert(rbt.root, Node(12))
    rbt.print(rbt.root, 0)
    print("\n")
    rbt.insert(rbt.root, Node(19))
    rbt.print(rbt.root, 0)
    print("\n")
    rbt.insert(rbt.root, Node(8))
    rbt.print(rbt.root, 0)
    #print(rbt.root.left.color)
    
main() 
