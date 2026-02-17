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

    ############### TESTING ######################
    # # build two root people and a child from them
    # parent1 = person_factory.build_person(PersonType.ROOT)
    # parent1.generation_rank = 1
    # parent2 = person_factory.build_person(PersonType.ROOT)
    # parent2.generation_rank = 1
    # child = person_factory.build_person(PersonType.CHILD, parent1=parent1, parent2=parent2, birth_year=1975)
    #
    # spouse = person_factory.build_person(PersonType.SPOUSE, person=parent1)
    #
    # # print results - testing
    # print(f'Parent 1: {parent1}')
    # print(f'Parent 2: {parent2}')
    # print(f'Child:    {child}')
    # print(f'Spouse:   {spouse}')
    ############### TESTING ######################

    tree_factory = FamilyTreeFactory(input_data=input_data, person_factory=person_factory)
    tree: FamilyTree = tree_factory.build_tree()

    print("Are you interested in: ")
    # get ui input from user
    FamilyTreeManagerUi(tree).start()


if __name__ == '__main__':
    family_tree_generator()
