from ui import FamilyTreeManagerUi
from family_tree import FamilyTree

def family_tree_generator():
    # generate family tree TODO
    # should use a builder class

    print('Reading files...')
    # read files

    print('Generating Family Tree...')
    # generate tree
    tree = FamilyTree()

    print("Are you interested in:")
    # get ui input from user

    FamilyTreeManagerUi(tree).start()


if __name__ == '__main__':
    family_tree_generator()
