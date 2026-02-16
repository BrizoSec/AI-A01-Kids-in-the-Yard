from ui import FamilyTreeManagerUi
from family_tree import FamilyTree
from input_extractor import InputExtractor


def family_tree_generator():
    """Generate a family tree and launch the interactive UI."""
    # generate family tree TODO
    # should use a builder class

    print('Reading files...')
    # read files
    input_data = InputExtractor().import_data()

    print('Generating Family Tree...')
    # generate tree
    tree = FamilyTree()

    print("Are you interested in:")
    # get ui input from user

    FamilyTreeManagerUi(tree).start()


if __name__ == '__main__':
    family_tree_generator()
