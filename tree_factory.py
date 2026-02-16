import random
import math
from family_tree import FamilyTree


class FamilyTreeFactory:
    """ Class to dynamically generate family trees."""

    def __init__(self, rnd_gen=None, input_data=None, person_factory=None):
        self.rnd_gen = rnd_gen if rnd_gen else random.Random()
        self.input_data = input_data
        self.tree = FamilyTree()
        self.person_factory = person_factory


    def build_tree(self):
        pass


    def build_children(self):
        pass

