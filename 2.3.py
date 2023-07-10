class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def deleteNode(head, num):
    previous = Node(None)
    current = head
    while current is not None:
        if current.data != num:
            pass
        elif current.data == num:
            previous.next = current.next
            return True
        previous = current
        current = current.next
    return False

def printList(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current=current.next

head = Node(3)
node2 = Node(2)
node3 = Node(5)
node4 = Node(4)
node5 = Node(1)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None

number = 2

print('\nlinked list before erasing: ' +str(number))
printList(head)
deleteNode(head, number)
print('\nlined list after removal of: ' +str(number))
printList(head)