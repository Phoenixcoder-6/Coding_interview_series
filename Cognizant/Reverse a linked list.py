class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
def reverse_iterative(head):
    prev= None
    current=head
    while current is not None:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move the 'prev' pointer forward
        current = next_node       # Move to the next node

    # When the loop finishes, 'prev' will be the new head of the reversed list
    return prev

# Function to print the linked list
def print_list(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Creating a sample linked list: 100 -> 200 -> 300 -> 400
node1 = Node(100)
node2 = Node(200)
node3 = Node(300)
node4 = Node(400)
node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
print_list(node1)

# Reversing the linked list iteratively
reversed_head = reverse_iterative(node1)

print("Reversed list (Iterative):")
print_list(reversed_head)
