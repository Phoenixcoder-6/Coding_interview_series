class Floyds_Cycle:
    def __init__(self,data):
        self.data=data
        self.next=None

def detect_cycle(head):
    slow,fast=head,head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    else:
        return None
    
    slow = head  # Move slow pointer back to head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow
    
node1=Floyds_Cycle(100)
node2=Floyds_Cycle(200)
node3=Floyds_Cycle(300)
node4=Floyds_Cycle(400)
node5=Floyds_Cycle(500)
node6=Floyds_Cycle(600)
node7=Floyds_Cycle(700)
node8=Floyds_Cycle(800)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7
node7.next=node8
node8.next=node3

head=node1


result=detect_cycle(head)
if result:
    print(f"Cycle detected at node with data: {result.data}")
else:
    print("No cycle detected")

