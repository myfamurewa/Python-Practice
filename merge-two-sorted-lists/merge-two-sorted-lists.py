class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = None
        resCur = None
        while l1 or l2:
            if (l1 and not l2) or (l1 and l1.val <= l2.val):
                if not result:
                    result = l1
                    resCur = l1
                else:
                    resCur.next = l1
                    resCur = resCur.next
                l1 = l1.next
            else:
                if not result:
                    result = l2
                    resCur = l2
                else:
                    resCur.next = l2
                    resCur = resCur.next
                l2 = l2.next
        return result