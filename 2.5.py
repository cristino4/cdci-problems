class Node: 
    def __init__(self,data):
        self.data = data
        self.next = None

def printList(head):
    current = head
    while current is not None:
        print(current.data, end=' ')
        current = current.next

#first number
head1 = Node(7)
node2_num1 = Node(1)
node3_num1 = Node(6)

head1.next = node2_num1
node2_num1.next = node3_num1
node3_num1 = None

#second number
head2 = Node(5)
node2_num2= Node(9)
node3_num2 = Node(2)

head2.next = node2_num2
node2_num2.next = node3_num2
node3_num2.next = None


# def add(first_head, second_head):

firstnumber = [1,2,3]
secondnumber = [5,6,7]

def add(n1, n2):
    add = 0
    carry = 0

    add = (n1[2] + n2[2])[0]