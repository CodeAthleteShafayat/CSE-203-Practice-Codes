class Node:
    def __init__(self,data):
        self.leftnode =  None
        self.rightnode = None
        self.data = data
class tree:
    def __init__(self):
        self.root = None
    def insert(self,node,value):
        if not node :
            node = Node (value)
            return node
        if value <= node.data:
            node.leftnode = self.insert(node.leftnode,value)
        else:
            node.rightchild = self.inset(node.rightchild,value)
        return node
    

    def insertbyloop(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            curr = self.root
            parent = None
            while curr:
                parent = curr
                if value <= curr.data :
                    curr = curr.leftleftnode
                else :
                    curr = curr.rightnode

                if curr.data <= parent.data:
                    parent.leftnode = curr.data
                else:
                    parent.rightnode = curr.data
        return self.root
    

    def  countallnode(self):
        count = 0
        if self.root is None:
            return count
        stack = [ ]
        curr = self.root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.leftnode
            else:
                curr = stack.pop()
                count += 1 
                curr = curr.rightnode
        return count
    def countallnodebyrecursion(self,node):
        count = 0
        if not node :
            return 0
        left_count = self.countallnodebyrecursion(node.leftnode)
        right_count = self.countallnodebyrecursion(node.rightnode)
        return 1 + left_count + right_count
    

    def searchiter(self,value):
        curr = self.root
        if not self.root:
            return
        while curr :
            print(curr.data, end="->")
            if curr.data == value:
                print("found")
            elif value<= curr.data:
                curr = curr.leftnode
            else:
                curr = curr.rightnode

        print("not found")

    def searchiterR(self,node,value):
        if not node:
            return
        print(node.data,end= "->")
        if node.data == value:
            print("found")
            return
        elif value<= node.data :
            self.searchiterR(node.leftnode,value)
        else:
            self.searchiterR(node.rightnode,value)
        print("not found")


    def searchitersum(self,node,value):
        if not node:
            return 0


        node += node.data
        if node.data == value:
            return node.data
            
        elif node.data >= value:
            return node.data + self.searchitersum(node.leftnode,value)
        else:
            return node.data + self.searchitersum(node.rightnode,value)

    def sum (self,value):
        if self.root is None:
            return 0
        curr = self.root
        sum = 0
        while curr:
            sum +=curr.data
            if curr.data == value:
                return sum
            elif value <= curr.data:
                curr = curr.leftnode
            else:
                curr = curr.rightnode
        return -1
    
    def printleaf(self,node):
        if not node:
            return
        self.printleaf(node.leftnode) 
        if node.leftnode is None and node.rightnode is None:
            print(node.data,end="->")
        self.printleaf(node.rightnode)
    leafnode = []
    def store_leaf_node(self,node):
        global leafnode
        if not node:
            return 
        else:
            self.store_leaf_node(node.leftnode)
            if not node.leftnode and not node.rightnode:
                leafnode.append(node.data)
            self.store_leaf_node(node.rightnode)

    def printoddleafs(self,node): 
        if not node:
            return 
        self.printoddleafs(node.leftnode)
        if not node.leftnode and not node.rightnode:
            if node.data %2 != 0 :
                print(node.data, end="->")
        self.printoddleafs(node.rightnode)
    
    def sumoddleafs(self,node):
        if not node:
            return 0
        self.sumoddleafs(node.leftnode)
        if not node.leftnode and not node.rightnode:
            if node.data % 2 != 0 :
                return node.data 
        self.sumoddleafs(node.rightnode)

    def sumoddleafss(self,node):
        if not node:
            return 0
        left_sum = self.sumoddleafss(node.leftnode)
        right_sum = self.sumoddleafss(node.rightnode)
        if node.leftndoe is None and node.rightnode is None:
            if node.data %2 != 0:
                return node.data
            else:
                return 0
        return left_sum + right_sum 
    

    def printsmallest(self,node):
        if not node:
            return
        curr = node
        while curr.leftnode:
            curr = curr.leftnode
        return curr.data 
    
    def printsmallest(self):
        if self.root is None:
            return 
        curr = self.root 
        while curr:
            if curr.leftnode is None:
                return curr.data
            curr = curr.leftnode
    
    def printsmallest(self,node):
        if not node:
            return 
        if node.leftnode is None:
            return node
        else:
            self.printsmallest(node.leftnode)



    def Elements_between(self,a ,b ):
        def helper(node):
            if not node :
                return 
            if a < node:
                helper(node.leftnode)
            if  a < node.data <b :
                print(node.data,"->")
            if node.data <=b:
                helper(node.rightnode)
        helper(self.root)



    def Element_between(self,a, b ):
        stack = []
        result = []
        node = self.root 
        while node or stack:
            while node :
                stack.append(node.data)
                node = node.leftnode
            node = stack.pop()
            if a < node.data <b :
                result.append(node.data)
            if node.data >= b:
                break
            node = node.rightnode
        print(result)



    def Element_between (self,a , b):
        stack = []
        result = []
        node = self.root 
        while node or stack:
            while node:
                if node.data > a :
                    stack.append(node.data)
                node = node.leftnode
                node = stack.pop(node.data)
                result.append(node)
                if node.data > b :
                    break
                else:
                    node = node.rightnode

    def Element_between (self,a , b):
        def helper(node):
            if not node :
                return 
            if  a < node.data :
                return helper(node.leftnode)
                if  a < node.data <= b :
                    print(node.data)
            if node.data < b :
                return helper(node.rightnode)
        helper(self.root)    
                    
    def find_sibling(self,a):
        if not self.root or self.root.data == a:
            return None
        curr = self.root
        while curr :
            if curr.lchild and curr.lchild.data == a  or  curr.rchild and curr.rchild.data == a  :
                if curr.lchild and curr.rchild:
                    if curr.lchild.data == a :
                        return curr.rchild 
                    else:
                        return curr.lchild
                else:
                    return None

            if a <= curr.data :
                curr = curr.lchild 
            else:
                curr = curr.rchild 

        return None
    

    def find_siblingR(self,node,a ):
        if not node or node.data == a :
            return None
        if (node.lchild and node.lchild.data == a) or (node.rchild and node.rchild.data == a ):
            if node.lchild and node.rchild :
                if node.lchild.data == a :
                    return node.rchild 
                else:
                    return node.lchild 
            else:
                return None

        if a < node.data:
            return self.find_siblingR(node.lchild, a )
        else:
            return self.find_siblingR (node.rchild, a )


        def update_first(heap):
            minimum = heap_extract_min(heap)   # removes root, fixes heap
            minimum += 5                        # increase by 5
            min_heap_insert(heap, minimum)      # re-insert, fixes heap
            return heap
        


        def delelte_odd(self):
            if self.head is None:
                return None
            curr = self.head 
            while curr:
                if curr.data % 2 != 0:
                    curr= curr.next
                    if curr :
                        curr.prev = None
                        self.head = curr 
                    else:
                        self.tail = None
                if curr.next and curr.next.data % 2 != 0 :
                    curr.next = curr.next.next
                    if curr.next :
                        curr.next.prev = curr 
                    else:
                        self.tail = curr 
                curr = curr.next
            return self.head
        



        def sum_leaf(self,node):
            if not node :
                return 0
            if not node.lchild and not node.rchild:
                return node.data 

            
            
            return  self.sum_leaf(node.lchild ) + self.sum_leaf(node.rchild)
        
        def check_cousin(root,node1,node2):
            if not root or root == node1.data or node2.data :
                return False
            check_cousin(root.lchild,node1,node2)
            if root.lchild.data == node1 and root.rchild.data ==node2 :
                return True
            return check_cousin(root.rchild,node1,node2)
            
            





            