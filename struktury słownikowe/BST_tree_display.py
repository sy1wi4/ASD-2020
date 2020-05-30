class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.parent=None
        self.left=None
        self.right=None


def insert(root,key,value):
    prev=None
    while root is not None :
        if key > root.key :
            prev=root
            root=root.right
        else:
            prev=root
            root=root.left

    if key < prev.key :
        prev.left=Node(key,value)
    else:
        prev.right=Node(key,value)
    

      
############################################################################################################
################################ PRINT TREE ################################################################
############################################################################################################


def display_tree(root):

    def print_tree(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.right is None and root.left is None:
                line = '%s' % root.key
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = print_tree(root.left)
                s = '%s' % root.key
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = print_tree(root.right)
                s = '%s' % root.key
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = print_tree(root.left)
            right, m, q, y = print_tree(root.right)
            s = '%s' % root.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2
        
    print()
    lines, _, _, _ = print_tree(root)
    for line in lines:
        print(line)
    print()



############################################################################################################
############################################################################################################
############################################################################################################

'''
  EXAMPLE:

                    ____100_
                   /        \
              ____66_      103____
             /       \            \
            33_     73_         _111____
           /   \       \       /        \
          23  43_     99      110     _145_
         /       \                   /     \
        20      62                  113   149__________
       /                                               \
      14                                             _182_
                                                    /     \
                                                  _176   196
                                                 /
                                               _166
                                              /
                                             157
   
   
  
'''                                             
