import heapq
heap = []
priority_queue = [(1,"Apple"), (3,"Banana"), (4,"Orange"), (2,"Grapes")]
class BinaryHeap:
    def insert(self, value):
        heapq.heappush(heap,value)
        print(f"item inserted : {value}")
    
    def remove_min(self):
        return f"min item removed : {heapq.heappop(heap)}"

    def heapify(self, items):
        heapq.heapify(items)
        return f"heapified list : {items}"
    
    def heappushpop(self, value):
        return f"pushed and popped item : {heapq.heappushpop(heap,value)}"
    
    def heapreplace(self, value):
        return f"replaced item : {heapq.heapreplace(heap,value)}"
    
    def nsmallest(self, n, iterable=heap, key=None):
        return f"{n} smallest items : {heapq.nsmallest(n,heap)}"
    
    def nlargest(self, n, iterable=heap, key=None):
        return f"{n} largest items : {heapq.nlargest(n,heap)}"
    

bh = BinaryHeap()
bh.insert(10)
bh.insert(3)
bh.insert(5)
print(heap)
print(bh.remove_min())
print(heap)
list1 = [1,3,5,2,4,6]
heap = [1,3,5,2,4,6]
print(bh.heapify(list1))
print(bh.nsmallest(1, heap))
print(bh.nlargest(2, heap))
heapq.heapify(priority_queue)
for i in range(len(priority_queue)):
    print(heapq.heappop(priority_queue))


