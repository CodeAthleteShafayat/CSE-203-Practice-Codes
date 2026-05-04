class heap:
    def __init__(self,array = None):
        self.array = array if array is not None else []
        self.heap_size = len(array)

    def parent(self, i ):
        if i % 2 == 0:
            return i //2 -1 
        else:
            return i //2
    def left(self,i):
        return (i * 2) + 1
    def righr(self, i ):
        return (i * 2) + 2
        
    def maxheapify(self,i):
        l = self.left(i)
        r  = self.right(i)
        largest = i 
        if l < self.heap_size and self.heap[l] > self.heap[largest] :
            largest = l
        if r < self.heap_size and self.heap[r] > self.heap[largest] :
            largest = r
        if i != largest :
            self.heap[i],self.heap[largest] = self.heap[largest],self.heap[i]

            self.maxheapify(largest)

    def add_at_root(heap):
        minimum = heap_extract_min(heap)
        minimum += 5
        min_heap_insert(heap,minimum)
        return heap
    
    def build_max_heap(self, value):
        for i in reversed(range(self.heap_size//2)):
            self.maxheapify(i)

    def heap_maximum(self):
        if self.heap_size <1 :
            return None
        return self.heap[0]
    def heap_extract_max(self):
        if self.heap_size <1:
            return None
        maximum = self.heap[0]
        self.heap[0] = self.heap[self.heap_size-1]
        self.heap.pop()
        self.heap_size -= 1
        self.maxheapify(0)
        return maximum
    
    def insert_max_heap(self,value):
        self.heap.append(value)
        self.heap_size += 1
        i = self.heap_size-1 
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.parent(i),self.heap[i] = self.heap[i],self.parent(i)
            i = self.parent(i)


    def inser_max_heap(self,value):
        self.heap.append(value)
        self.heap_size += 1
        self.maxheapify(value)
        
class heap:
    def __init__(self,array = None):
        self.array = array if array else []
        self.heap_size = len(self.heap)
        if array:
            return self.build_max_heap()
    def parent(self,i):
        if self.heap_size %2 ==0 :
            return (i-1 // 2) 
        else:
            return i//2
    def left (self, i ):
        return 2 *i +1
    def right (self, i ):
        return 2 * i + 2 
    def max_heapify(self , i ):
        l = self.left(i)
        r = self.right(i)
        largest = i
        if l < self.heap_size and self.heap[l] > self.heap[largest] :
            largest = l
        if r < self.heap_size and self.heap[r] > self.heap[largest] :
            largest = r
        if largest != i :
            self.heap[largest],self.heap[i] = self.heap[i] , self.heap[largest]
            self.max_heapify(largest)

    def mean_heap(self,array ):
        n = len(array)
        for i in range(n // 2 -1,-1,-1):
            self.min_heapify(array)
        return array
        

    
    def delete_lst_3rd(self):
        count = 1
        curr = self.tail 
        while curr.prev:
            if count ==3 :
                curr.prev = curr.prev.prev
                if curr.prev:
                    curr.prev.next = curr
                else:
                    self.head = curr
                

            curr = curr.prev
            count += 1

    def delete (self):
        delnode = self.tail.prev.prev
        delnode.prev.next = delnode.next
        delnode.next.prev = delnode.prev
        