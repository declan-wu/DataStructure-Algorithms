# preorder traversal
from bin_tree import BinaryTree


def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


def inorder(tree):
    if tree:
        preorder(tree.getLeftChild())
        print(tree.getRootVal())
        preorder(tree.getRightChild())


def postorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


r = BinaryTree('a')
r.insertLeft('4')
preorder(r)
