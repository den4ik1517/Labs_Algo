from BinaryTree import BinaryTree, invert_binary_tree

def are_binary_trees_equal(tree1, tree2):
    if tree1 is None and tree2 is None:
        return True
    if tree1 is None or tree2 is None:
        return False
    return (tree1.value == tree2.value and
            are_binary_trees_equal(tree1.left, tree2.left) and
            are_binary_trees_equal(tree1.right, tree2.right))

def test_invert_binary_tree():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    expected_inverted_root = BinaryTree(1)
    expected_inverted_root.left = BinaryTree(3)
    expected_inverted_root.right = BinaryTree(2)
    expected_inverted_root.left.left = BinaryTree(7)
    expected_inverted_root.left.right = BinaryTree(6)
    expected_inverted_root.right.left = BinaryTree(5)
    expected_inverted_root.right.right = BinaryTree(4)

    inverted_root = invert_binary_tree(root)

    assert are_binary_trees_equal(inverted_root, expected_inverted_root)

    print("Тест виконано успішно")

if __name__ == "__main__":
    test_invert_binary_tree()
