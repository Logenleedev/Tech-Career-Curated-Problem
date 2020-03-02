# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Linkedlist:
    def __init__(self, head=None):
        self.head = None

    def addElement(self, element):
        element.next = self.head
        self.head = element

    # Iterative Method
    def reverseList(self):
        prev = None
        while self.head:
            nextElement = self.head.next
            self.head.next = prev
            prev = self.head
            self.head = nextElement
        self.head = prev
    # Recursive Method
    def reverseListRecursive(self, head):
        # case1: empty list
        if head is None:
            return head
        # case2: only one element list
        if head.next is None:
            return head
        # case3: reverse from the rest after head
        newHead = self.reverseListRecursive(head.next)
        # reverse between head and head->next
        head.next.next = head
        # unlink list from the rest
        head.next = None

        return newHead

    def printList(self):
        result = ""
        while self.head:
            result = result + str(self.head.val) + "->"
            self.head = self.head.next
        print(result)


test = Linkedlist()
test.addElement(ListNode(1))
test.addElement(ListNode(2))
test.addElement(ListNode(3))
test.addElement(ListNode(4))
test.addElement(ListNode(5))
# test.reverseList()
test.reverseListRecursive(ListNode(5))
test.printList()
