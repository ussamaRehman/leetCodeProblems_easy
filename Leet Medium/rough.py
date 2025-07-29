# let's say we have a linked list with 5 nodes, and head points to first node
# now tell me, what the following code outputs
head = [1, 2, 3, 4, 5] 
current = head
length = 0
n = 2
while current:
    length += 1
    current = current.next

current = head

for _ in range(length - n):
    current = current.next


