# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        values = []
        current = head
        while current is not None:
            values.append(current.val)
            current = current.next
        values = sorted(values)
        print(values)
        current = head
        nextNode = None
        for i in range(len(values)):
            if values[i] != current.val:
                current.val = values[i]
            current = current.next
        return head