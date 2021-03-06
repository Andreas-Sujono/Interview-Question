# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        result = ListNode(0)
        root = result
        
        while(l1 or l2 or carry):
            temp1 = l1.val if l1 else 0
            temp2 = l2.val if l2 else 0
            result.next = ListNode((temp1 + temp2 + carry) % 10)
            carry = (temp1 + temp2 + carry)//10
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            result = result.next
            
        return root.next

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while (result):
    print (result.val, end=' ')
    result = result.next
print()
# 7 0 8