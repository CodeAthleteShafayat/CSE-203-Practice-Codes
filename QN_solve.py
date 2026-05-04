def sumR_DLL(head):
    if not head:
        return 0
    return head.data + sumR_DLL(head.next)

def sum(self,head):
    curr = head
    sum = 0
    while curr:
        sum += curr.data
        curr = curr.next
    return sum 


def below60(self,node = None ):
    if not node:
        node = self.root 
    if not node :
        return
    if not node.lchild and not node.rchild:
        if node.data < 60:
            print(node.data,end =" ")
        return
    self.below60(node.lchild)
    self.below60(node.rchild) 

def find_sibling(self,a):
    def helper(node):
        if not node:
            return 
        if node.lchild :
            pass

def find_sibling(self,a ):
    if not self.root:
        return 
    curr = self.root
    while curr.lchild or curr.rchild :   
        if curr.lchild.data == a :
            if curr.rchild :
                return curr.rchild 
            else:
                return None
        if curr.rchild.data == a :
            if curr.lchild :
                return curr.lchild
            else:
                return None
            
        if curr.data > a :
            curr = curr.lchild 
        else:
            curr = curr.rchild 

def find_sibling(self,a):
    if not self.root or self.root.data == a :
        return None
    curr = self.root 
    parent = None
    while curr:
        parent = curr
        if curr.data == a :
            if parent.lchild and parent.rchild :
                if parent.lchild.data == a:
                    return parent.rchild 
                else:
                    return parent.lchild 
            else:
                return None
        if curr.data > a :
            curr = curr.lchild 
        else:
            curr = curr.rchild     
        
            