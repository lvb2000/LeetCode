from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # go for a seperate ListNode in python do not replace
        dummy = ListNode()
        curr = head

        while curr:
            value = curr.val
            if dummy.next is None:
                dummy.next = ListNode(val=value)
                curr = curr.next
                continue

            prev_dummy = dummy
            curr_dummy = prev_dummy.next
            # [0,4]
            while curr_dummy:
                if value < curr_dummy.val:
                    # insert
                    # [4,6,5] -> [4]
                    # [4,6,5] -> [4,6]
                    # [4,6,5] -> [4,5,6] 4->5 5->6; 4=prev_dummy 5=curr_dummy 4=node.val
                    # new entry
                    entry = ListNode(val=value)
                    prev_dummy.next , entry.next = entry , curr_dummy
                    break
                if curr_dummy.next is None:
                    entry = ListNode(val=value)
                    curr_dummy.next = entry
                    break
                prev_dummy = prev_dummy.next
                curr_dummy = curr_dummy.next


            curr = curr.next
        return dummy.next

def printLL(head):
    res = '['
    while head:
        res += str(head.val)
        head = head.next
        if head:
            res+= ', '
    print(res + ']')


if __name__ == "__main__":
    head = ListNode(4)
    head.next = ListNode(6)
    head.next.next = ListNode(5)
    head.next.next.next = ListNode(3)
    print("Input:")
    printLL(head)
    s = Solution()
    print("Output:")
    printLL(s.insertionSortList(head))
