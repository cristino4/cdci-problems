class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    if head is None:
        return head

    # Create a set to store unique values
    unique_values = set()

    current = head
    print('\nbeginning node\n', current)
    unique_values.add(current.data)

    while current.next is not None:
        if current.next.data in unique_values:
            # Skip the duplicate node
            current.next = current.next.next
            print('next node: ',current.next)
        else:
            # Add the data to the set and move to the next node
            unique_values.add(current.next.data)
            print('\nnew data added ' + str(current.next.data))
            current = current.next

    return head

# Example usage

# Create a sample linked list with duplicates
head = Node(1)
node1 = Node(2)
node2 = Node(3)
node3 = Node(2)
node4 = Node(4)
node5 = Node(1)

head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before removing duplicates:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 3 2 4 1

head = remove_duplicates(head)

print("\nAfter removing duplicates:")
current = head
while current is not None:
    print(current.data, end=" ")
    current = current.next
# Output: 1 2 3 4
