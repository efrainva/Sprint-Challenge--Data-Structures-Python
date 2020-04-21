class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None
  #                       value of node
  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we
    # traverse the list
    current = self.head
    # check to see if we're at a valid node
    while current:
      # return True if the current value we're looking at matches our
      # target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  #                       the node it self block  
  def reverse_list(self, node = None , prev = None):# node, prev done call the vairables till later
    
    # if node is None:
    #   return
    
    # if node.get_next() == None:
    #   self.head = node
    #   self.head.next_node = prev

    #   return

    # self.reverse_list(node.get_next(), node)
    # node.next_node = prev

    prev_node = None
    current_node = self.head
    while current_node is not None:
      next_node = current_node.get_next()
      current_node.set_next(prev_node)
      prev_node = current_node
      current_node = next_node
    self.head = prev_node

  # current_node = node 
  # if current_node is not None:
  #   next_node = current_node.get_next()
  #   current_node.set_next(prev_node)
    
  #   self.reverse_list( ,prev_node)


    # current = self.head
    # if current == None:
    #   return 

    # if current.get_next() == None:
    #   self.head = current
    #   return self.head
    # # print(node,prev)
    # nodeone = self.reverse_list(current.get_next(),next)
    # current.get_next().set_next(current)
    # current.set_next(None)
    # return nodeone

  # def get(self):
  #   arr = []
  #   current = self.head
  #   # print(current)
  #   while  current : 
  #     arr.append(current.value)
  #     current = current.next

  #   return arr

# one = Node(4,2)
# # one.get_value()
# # one.get_next()
lin = LinkedList()
lin.add_to_head(3)
lin.add_to_head(4)
lin.add_to_head(7)
lin.add_to_head(5)
# lin.get()
# lin.reverse()
lin.reverse_list()