from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode()
        curr = head

        while curr:
            # At each iteration, we insert an element into the resulting list.
            prev = dummy

            # find the position to insert the current node
            while prev.next and prev.next.val <= curr.val:
                prev = prev.next

            next = curr.next
            # insert the current node to the new list
            curr.next = prev.next
            prev.next = curr

            # moving on to the next iteration
            curr = next

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