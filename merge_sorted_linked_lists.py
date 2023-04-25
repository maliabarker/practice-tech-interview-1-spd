"""
Given two sorted linked lists, merge them so that the resulting linked list is also sorted.
EXAMPLE:
input:
head1 > 4 > 8 > 15 > 19 > null
head2 > 7 > 9 > 10 > 16 > null
output:
head > 4 > 7 > 8 > 9 > 10 > 15 > 16 > 19 > null
"""

"""
Assumptions/Questions:
    Is this is singly or doubly linked list?
    Do you want me to code my own linkedlist and node classes?
    If we don't implement our own linked list, do we assume the list has a head AND a tail attribute?
    Are we creating a new linked list or are we modifying one of the existing lists?

Pseudocode
    First, I would start by making my own node and linked list classes. 
    I would make sure to add head and tail so I can keep track of both.

    For the function, I would need to traverse over both lists. 
    I would do this by only looking at the head nodes and once the head node 
	is added to our new merged list, I would get rid of it by making the next 
	node the head node.
	In this traversal, I would compare the values of the head nodes and append 
	whichever is smaller first.
	Once one of the lists is empty (meaning the head is None), we would check to 
	see if there is anything left in either list.
	If there is, we just traverse over the nodes remaining and append them to 
	the returned list.
"""

class Node():
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList():
	def __init__(self):
		self.head = None
		self.tail = None
		self.count = 0
		
	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while (last.next):
			last = last.next
		last.next = new_node

	def print_list(self):
		current_node = self.head
		while current_node is not None:
			print (current_node.data)
			current_node = current_node.next


def merge_sorted_linked_lists(ll1, ll2):
	merged_ll = LinkedList()
	# start with base case, which is that both linked lists are empty, return empty linkedlist
	if ll1.head is None and ll2.head is None:
		return merged_ll
	
	# continue the comparisons until there is nothing left in at least one of the lists
	while ll1.head is not None and ll2.head is not None:
		# compare the head nodes
		if ll1.head.data > ll2.head.data:
			# the second head is less than the first, add as next element in merged list
			merged_ll.append(ll2.head.data)
			# then increment this linked list by getting rid of the head node we just added
			ll2.head = ll2.head.next
			print('Making next node:', ll2.head)
		else:
			# the first head is less than the second, add as next element in merged list
			merged_ll.append(ll1.head.data)
			# then increment this linked list by getting rid of the head node we just added
			ll1.head = ll1.head.next
			print('Making next node:', ll1.head)

	# check to see if there is anything left over in the lists and if there is, append everything
	current_node_1 = ll1.head
	while (current_node_1):
		merged_ll.append(current_node_1.data)
		current_node_1 = current_node_1.next

	current_node_2 = ll2.head
	while (current_node_2):
		merged_ll.append(current_node_2.data)
		current_node_2 = current_node_2.next
    
	# return the merged linked list
	return merged_ll

ll1 = LinkedList()
ll1.append(4)
ll1.append(8)
ll1.append(15)
ll1.append(19)
ll1.print_list()

ll2 = LinkedList()
ll2.append(7)
ll2.append(9)
ll2.append(10)
ll2.append(16)
ll2.print_list()

merged_list = merge_sorted_linked_lists(ll1, ll2)
merged_list.print_list()