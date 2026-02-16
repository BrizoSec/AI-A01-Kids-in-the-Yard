from ui import FamilyTreeManagerUi
from family_tree import FamilyTree
from input_extractor import InputExtractor
from person_factory import PersonFactory, PersonType
from tree_factory import FamilyTreeFactory

def family_tree_generator():
    """Generate a family tree and launch the interactive UI."""

    print('Reading files...')
    # read files
    input_data = InputExtractor()

    # build person and tree factories
    print('Generating Family Tree...')
    person_factory = PersonFactory(input_data=input_data)
    print(person_factory.build_person(PersonType.ROOT))

    tree_factory = FamilyTreeFactory(input_data=input_data, person_factory=person_factory)
    tree: FamilyTree = tree_factory.build_tree()

    print("Are you interested in: ")
    # get ui input from user
    FamilyTreeManagerUi(tree).start()


if __name__ == '__main__':
    family_tree_generator()
