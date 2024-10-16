class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=Node(100)
node2=Node(200)
node3=Node(300)
node4=Node(400)
node1.next= node2
node2.next=node3
node3.next=node4

code1= Node(700)
code2=Node(800)
code3= Node(900)
code4= Node(1000)
code1.next= code2
code2.next=code3
code3.next= code4

head=node1
head1= code1


def merge(head,head1):
    
    current= head
    while current.next is not None:
        current=current.next
    current.next=head1

    return head

def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Merging the two lists
merged_head = merge(node1, code1)

# Printing the merged linked list
print_list(merged_head)


