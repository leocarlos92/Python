
class node:
    def __init__(self, value = None):
        self.value = value
        self.left_child = None
        self.right_child = None
        # self.parent = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value<cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = node(value)
                cur_node.left_child.parent = cur_node
            else:
                self._insert(value, cur_node.left_child)
        elif value>cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = node(value)
                cur_node.right_child.parent = cur_node
            else:
                self._insert(value, cur_node.right_child)
        else:
            print "Value already in tree!"

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.left_child)
            print str(cur_node.value)
            self._print_tree(cur_node.right_child)

    def height(self):
        if self.root is not None:
            return self._height(self.root, 0)
        else:
            return 0

    def _height(self, cur_node, cur_height):
        if cur_node is None:
            return cur_height
        left_height = self._height(cur_node.left_child, cur_height+1)
        right_height = self._height(cur_node.right_child, cur_height+1)
        return max(left_height, right_height)

    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    def _search(self, value, cur_node):
        if value == cur_node.value:
            return True
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._search(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._search(value, cur_node.right_child)
        return False

    def find(self, value):
        if self.root is not None:
            return self._find(value, self.root)

    def _find(self, value, cur_node):
        if value is not None:
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            return self._find(value, cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            return self._find(value, cur_node.right_child)

    # def delete_value(self, value):
    #     return self.delete_node(self.find(value))
    #
    # def delete_node(self, node):
    #
    #     def min_value_node(n):
    #         current = n
    #         while current.left_child is not None:
    #             current = current.left_child
    #         return current


def fill_tree(tree, num_elems = 100, max_int = 1000):
    from random import randint
    for _ in range(num_elems):
        cur_element = randint(0, max_int)
        tree.insert(cur_element)
    return tree


tree = binary_search_tree()
tree = fill_tree(tree)

# tree.insert(5)
# tree.insert(1)
# tree.insert(3)
# tree.insert(2)
# tree.insert(7)
# tree.insert(10)
# tree.insert(0)
# tree.insert(20)

tree.print_tree()
print "Tree height is: {}".format(tree.height())
print tree.search(10)
print tree.search(30)