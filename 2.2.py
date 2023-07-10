class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_kth_to_last_element(head, k):
    ptr1 = head
    ptr2 = head

    # Move ptr2 ahead by k positions
    for _ in range(k):
        if ptr2 is None:
            return None  # k is greater than the number of elements in the list
        ptr2 = ptr2.next
    
    # Move both pointers simultaneously until ptr2 reaches the end
    while ptr2.next is not None:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1.data

# Example usage:
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

k = 2
result = find_kth_to_last_element(head, k)
print(f"The {k}th to last element is: {result}")
