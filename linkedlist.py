#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

   
    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

   
    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

   
    def is_empty(self):
        """Runs at 0(1) in best and worst case scenarios"""
        return self.head is None

   
    def length(self):
        """This method runs at 0(n) at best/worst case scenario"""
 
        count = 0
        node = self.head    

        while node is not None:
            count += 1
            node = node.next  
        
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list."""
        """The best case scenario will run at 0(1) and the worst case scenario will run at 0(N)"""
       
        new_node = Node(item)
       
        if self.tail is not None:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node

   
    def prepend(self, item):
        """The best case scenario will run at 0(1), the worst case scenario is 0(N)"""
  
        new_node = Node(item)
       
        if self.head is not None:
            new_node.next = self.head
        else:
            self.tail = new_node
        self.head = new_node


    def find(self, quality):
        """Best case running time: O(1) Item is the first item in the list will be a since look up?
           Worst case running time: O(N) Item is last in list or not in list at all. Has to traverse entire linkedlist"""
            
        node = self.head

        while node is not None:
            if quality(node.data) == True:
                return node.data
            else:
                node = node.next

        return None


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        Best case running time: O(1) First item is deleted
        Worst case running time: O(N) Last item is deleted. Entire list must be traversed"""
       
        # starting points
        current_node = self.head
        previous_node = None

        # while node is not empty data 
        while current_node is not None:

            #node with item has been found
            if item == current_node.data:

                #if iteam is head 
                if previous_node is None:
                    # make head next to node
                    self.head = current_node.next

                    # head is tail
                    if current_node.next is None:
                        self.tail = previous_node
                #item to remove is at tail
                elif current_node.next is None:
                    previous_node.next = None
                    self.tail = previous_node

                #item we want to remove is not an edge case
                else:
                    #make previous node to next node
                    previous_node.next = current_node.next

                return
            #item has not been found yet advance pointers
            else:
                previous_node = current_node
                current_node = current_node.next

        raise ValueError(f'Item not found: {item}')


def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()