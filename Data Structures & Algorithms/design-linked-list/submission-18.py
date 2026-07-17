class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left


    def get(self, index: int) -> int:
        print(f"curremt index", index)
        cur = self.left.next
        while cur and index > 0 and cur!= self.right.prev:
            cur = cur.next
            index -=1
        if cur and index == 0:
          
            print(f"my current val", cur.val)
            print(f"my current prev val", cur.prev.val)

            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        cur, prev, next = Node(val), self.left, self.left.next
        prev.next = cur
        next.prev = cur
        cur.next = next
        cur.prev = prev

    def addAtTail(self, val: int) -> None:
        cur, prev, next = Node(val), self.right.prev, self.right
        prev.next = cur
        next.prev = cur
        cur.next = next
        cur.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -=1
        if cur and index == 0:
            node, prev, next = Node(val), cur.prev, cur
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -=1
        if cur and index == 0 and cur != self.right:
            prev, next = cur.prev, cur.next
            prev.next = next
            next.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)