class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

def check_middle(head):
    if head is not None:
        slow=head
        fast=head

        while fast is not None and fast.next is not None:

            slow=slow.next
            fast=fast.next.next

        return slow.data
    else:
        return None
    
node1=Node(100)
node2=Node(200)
node3=Node(300)
node4=Node(400)
node5=Node(500)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Finding and printing the middle element
middle_element = check_middle(node1)
print("Middle element:", middle_element)