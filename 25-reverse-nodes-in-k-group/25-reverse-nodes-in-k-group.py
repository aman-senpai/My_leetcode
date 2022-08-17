# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gPrev = dummy
        
        while True:
            kth = self.getKth(gPrev, k)
            if not kth: break
            gNext = kth.next
            
            # reverse group
            prev, curr = kth.next, gPrev.next
            while curr != gNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = gPrev.next
            gPrev.next = kth
            gPrev = tmp
        return dummy.next
            
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr