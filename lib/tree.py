class Tree:
  def __init__(self, root = None):
    self.root = root

#use the depth-first approach
#take a string as argument.
#return the node with that value
#if matching node is not found, return None
#once pasisng, modify for breadth-first traversal (tests should still pass)
  #Depth-first
  # def get_element_by_id(self, id):
  #   to_visit = [self.root]
  #   while to_visit:
  #     node = to_visit.pop()
  #     if node['id'] == id:
  #       return node
  #     to_visit = node['children'] + to_visit
  #   return None

  #Breadth-first
  def get_element_by_id(self, id):
    to_visit = [self.root]
    while to_visit:
      node = to_visit.pop()
      if node['id'] == id:
        return node
      to_visit = to_visit + node['children']
    return None
