class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    # Initialize a dummy node and a current pointer
    dummy = ListNode()
    current = dummy
    
    # Traverse both lists until one is exhausted
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Append the remaining list (if any)
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    # Return the merged list, which starts after the dummy node
    return dummy.next

a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(8)
a.next.next.next = ListNode(9)

# Create another hard-coded linked list:
# 1 -> 3 -> 8 -> 10
b = ListNode(1)
b.next = ListNode(3)
b.next.next = ListNode(8)
b.next.next.next = ListNode(10)

merged_list = mergeTwoLists(a, b)

temp = merged_list
print("Merged Link List is:")
while temp:
    print(temp.val, end=" ")
    temp = temp.next
