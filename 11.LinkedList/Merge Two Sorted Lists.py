
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
l3head = curr = ListNode(0)

while l1 and l2:
    if l1.val < l2.val:
        curr.next = l1
        l1 = l1.next
    else:
        curr.next = l2
        l2 = l2.next
    curr = curr.next
curr.next = l1 or l2

return l3head.next


"""
Test cases:
[1,2,4]
[1,3,4]
[]
[]
[]
[0]

output:
[1,1,2,3,4,4]
[]
[0]

"""
