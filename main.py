from ui import FamilyTreeManagerUi
from family_tree import FamilyTree
from input_extractor import InputExtractor
from person_factory import PersonFactory, PersonType


def family_tree_generator():
    """Generate a family tree and launch the interactive UI."""
    # generate family tree TODO
    # should use a builder class

    print('Reading files...')
    # read files
    input_data = InputExtractor()

    # test person factory
    factory = PersonFactory(input_data=input_data)
    person = factory.build_person(PersonType.ROOT)
    print(person)

    print('Generating Family Tree...')
    # generate tree
    tree = FamilyTree()

    print("Are you interested in: ")
    # get ui input from user
    FamilyTreeManagerUi(tree).start()


if __name__ == '__main__':
    family_tree_generator()
