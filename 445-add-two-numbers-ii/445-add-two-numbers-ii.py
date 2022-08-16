# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = n2 = 0
        ptr1, ptr2 = l1, l2         # Pointers to the head of the given two lists
        stack = []                  # Maintaining the stack to reverse it in the end
        
        while ptr1: n1 += 1; ptr1 = ptr1.next   # counting the nuber of nodes in l1
        while ptr2: n2 += 1; ptr2 = ptr2.next   # counting the number of nodes in l2
        max_len = n1 if n1 > n2 else n2     # taking the max value of two
        
        while max_len:
            v1 = v2 = 0
            if max_len <= n1: v1 = l1.val; l1 = l1.next
            if max_len <= n2: v2 = l2.val; l2 = l2.next
            stack.append(v1 + v2)
            max_len -= 1
        
        val, head = 0, None
        while stack or val:
            if stack: val += stack.pop()
            node = ListNode(val % 10)        # adding the single digit
            node.next = head
            head = node
            val //= 10                      # getting the carry
        return head 