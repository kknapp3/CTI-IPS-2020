### do not modify this class
class LinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None

### do not modify this class, or any of the methods in it, other than reverse()
### you may insert new methods if you like
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def empty(self):
        return self.head == None
    
    def append(self, data):
        if self.empty():
            self.head = LinkedNode(data)
            self.tail = self.head
        else:
            new_node = LinkedNode(data)
            self.tail.next = new_node
            self.tail = new_node
      
    def extend(self, array):
        for element in array:
            self.append(element)
  
  # used in test cases verify correct solutions
  # if you want to test your code without submitting, consider using this function
    def to_array(self):
        array = []
        curr = self.head
        while curr != None:
            array.append(curr.data)
            curr = curr.next
        return array
  
  # implement this method
    def reverse(self):
        stack = []
        curr = self.head
        while curr != None:  # load data onto stack
            stack.append(curr.data)
            curr = curr.next
        self.head = self.tail = None  # empty linked list
        while stack:  # pop data off stack to append to list
            self.append(stack.pop())


# # # # # #  RECURSIVE SOLUTION  # # # # # # # # #
#
#    if self.empty() or self.head.next == None:
#      return self
#    first = self.head
#    self.head = self.head.next
#    self.reverse()
#    return self.append(first.data)
#
# # # # # # # # # # # # # # # # # # # # # # # # #

# # # # # #  ITERATIVE SOLUTION  # # # # # # # # #
#
#    self.head = self.tail
#    self.tail = first
#    second = first.next
#    self.tail.next = None
#    while second != None:
#      third = second.next
#      second.next = first
#      first = second
#      second = third
#
# # # # # # # # # # # # # # # # # # # # # # # # #


ll = LinkedList()
ll.extend(range(994))
print(ll.to_array())
ll.reverse()
print(ll.to_array())