def atoi(s):
    rtr, sign=0, 1
    s = s.strip()
    if s[0] in '+-':
        sc, s=s[0], s[1:]
        if sc=='-':
            sign=-1

    for c in s:
        rtr=rtr*10 + ord(c) - ord('0')

    return sign*rtr

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
        self.total = 0
        self.nb = 0
        self.bh = 0
    def insert(self, tree, n):
        if self.root.val is None:
            self.root = n
            self.expand(n)
            self.total += 1
        elif n.val < tree.val:
            if tree.left.val is None:
                tree.left = n
                n.parent = tree
                self.expand(n)
                self.total +=1
            else:
                self.insert(tree.left, n)
        else:
            if tree.right.val is None:
                tree.right = n
                n.parent = tree
                self.expand(n)
                self.total += 1
            else:
                self.insert(tree.right, n)
        n.color = 'red'
        self.fixup(tree, n)

    def search(self, n, val):
        if(n.val is None):
            return Exception
        if(n.val is val):
            return n
        elif(n.val > val):
            if(n.left is None):
                return Exception
            else:
                return self.search(n.left, val)
        elif(n.val < val):
            if(n.right is None):
                return Exception
            else:
                return self.search(n.right, val)
    
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

    def minimum(self, x):
        if(x.left.val is None):
            return x
        else:
            return self.minimum(x.left)

    def print(self,tree,level):
        if(level > self.bh):
            self.bh = level
        if tree.right is not None:
            self.print(tree.right,level + 1)
        for i in range(level):
            print('   ', end='')
        print(tree.val,' , ',tree.color)
        if(tree.color is 'black'):
            self.nb += 1
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

    def transplant(self, u, v):
        if(u.parent is None):
            self.root = v
        elif(u is u.parent.left):
            u.parent.left = v
        else:
            u.parent.right = v
        if(v is not None):
            v.parent = u.parent

    def delete(self, z):
        y = z
        original = y.color
        if(z.left.color is None):
            x = z.right
            self.transplant(z, z.right)
        elif(z.right.color is None):
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            original = y.color
            x = y.right
            if(y.parent is z):
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if(original is 'black'):
            self.delete_Fixup(x)
        self.total -= 1

    def delete_Fixup(self, x):
        while(x is not self.root and x.color is 'black'):
            if(x is x.parent.left):
                w = x.parent.right
                if(w.color is 'red'):
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.leftRotate(x.parent)
                    w = x.parent.right
                if(w.left.color is 'black' and w.right.color is 'black'):
                    w.color = 'red'
                    x = x.parent
                else:
                    if(w.right.color is'black'):
                        w.left.color = 'black'
                        w.color = 'red'
                        self.rightRotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    self.leftRotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if(w.color is 'red'):
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rightRotate(x.parent)
                    w = x.parent.left
                if(w.right.color is 'black' and w.left.color is 'black'):
                    w.color = 'red'
                    x = x.parent
                else:
                    if(w.left.color is'black'):
                        w.right.color = 'black'
                        w.color = 'red'
                        self.leftRotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    self.rightRotate(x.parent)
                    x = self.root
            x.color = 'black'
    
def main():

    rbt = RBT()
    error = 0
    f = open("input.txt", 'r')
    lines = f.readlines()
    for line in lines:
        line = atoi(line)
        if(line > 0):
            rbt.insert(rbt.root, Node(line))
        elif(line < 0):
            line = abs(line)
            delete = rbt.search(rbt.root, line)
            
            if(delete is Exception or delete is None):
                error += 1
            else:
                rbt.delete(delete)
        else:
            break
    f.close()
    print('----------------------------------')
    rbt.print(rbt.root, 0)
    print('----------------------------------')
    print(rbt.total)
    print(rbt.nb)
    print(rbt.bh / 2)
main() 
