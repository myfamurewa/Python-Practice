# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:

        # We want to "rotate" the linked list. 
        # This means we want to move k elements from the end of the linked list to beginning
        # remove the last k elements of the ll
        # append the elements to the head in the order they were removed
        # return the head
        
        def removal(k: int) ->  list:
            nonlocal head
            current = head
            previous = None
            nextnode = None
            count = 0
            removed = []
            while current is not None:        
                count += 1 
                previous = current 
                nextnode = current.next 
                current = nextnode
            removal_start = count - k
            current = head
            previous = None
            nextnode = None
            count = 0
            while current is not None:
                if count >= removal_start:
                    removed.append(current.val)
                    previous.next = current.next
                    current.next = None
                    current = previous
                count += 1
                previous = current 
                nextnode = current.next
                current = nextnode
            return removed
        def addition(removed):
            nonlocal head
            removed = removed[::-1]
            for value in removed:
                newnode = ListNode(value, head)
                head = newnode
        addition(removal(k))
        return head

    def rotateRightV2(self, head: ListNode, k: int) -> ListNode:
        # def findTail(head: ListNode) -> ListNode:
        #     current = head
        #     previous = None
        #     nextnode = None
        #     while current is not None:        
        #         previous = current 
        #         nextnode = current.next 
        #         current = nextnode
        #     return previous

        # tail = findTail(head)

        def count() -> int:
            nonlocal head
            if head is None:
                return 0
            elif head is not None and head.next is None:
                return 1
            current = head
            previous = None
            nextnode = None
            count = 0
            removed = []
            while current is not None:        
                count += 1 
                previous = current 
                nextnode = current.next 
                current = nextnode
            return count 

        def removeAndAddToHead() -> ListNode:
            nonlocal head
            if head is None or head.next is None:
                return
            secondlast = head
            while secondlast.next.next is not None:
                secondlast = secondlast.next
            lastnode = secondlast.next
            secondlast.next = None
            newnode = ListNode(lastnode.val, head)
            head = newnode
            return None
        rotations = 0
        length = count()
        if k == 0:
            return head
        if length == 0:
            return head
        while rotations < k % length:
            removeAndAddToHead()
            rotations += 1
        return head
                