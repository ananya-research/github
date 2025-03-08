# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy=ListNode()
        cur=dummy

        while list1 and list2:
            v1=list1.val if list1 else 0
            v2=list2.val if list2 else 0

            if v1<v2:
                val=v1
                cur.next=ListNode(val)
                cur=cur.next
                list1=list1.next
            else:
                val=v2
                cur.next=ListNode(val)
                cur=cur.next
                list2=list2.next

        cur.next=list1 if list1 else list2

        return dummy.next


