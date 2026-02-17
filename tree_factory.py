import random
import math
from family_tree import FamilyTree
from person_factory import PersonType


class FamilyTreeFactory:
    """ Class to dynamically generate trees """

    def __init__(self, rnd_gen=None, input_data=None, person_factory=None):
        self.rnd_gen = rnd_gen if rnd_gen else random.Random()
        self.input_data = input_data
        self.tree = FamilyTree()
        self.person_factory = person_factory

    # hard coding max year for now
    # TODO - make this a variable that can be edited in CLI
    MAX_YEAR = 2120
    DEF_BIRTH_RATE = 2.0
    DEF_MAR_RATE = .4

    def build_tree(self):
        """Build a family tree starting from a root couple born in 1950 until 2120."""

        # create roots
        parent1 = self.person_factory.build_person(PersonType.ROOT)
        parent2 = self.person_factory.build_person(PersonType.ROOT)

        # set ranks to initial (1)
        parent1.generation_rank = 1
        parent2.generation_rank = 1

        # set spouses for roots
        parent1.spouse = parent2
        parent2.spouse = parent1

        # add roots to tree
        self.tree.add_root(parent1)
        self.tree.add_root(parent2)

        # build out the rest
        self.build_children(parent1, parent2)

        return self.tree


    def build_children(self, parent1, parent2):
        """Build children and families until MAX_YEAR is reached."""

        decade = f"{parent1.yr_born - (parent1.yr_born % 10)}s"
        birth_rate = self.input_data.birth_rate_data.get(decade, self.DEF_BIRTH_RATE)

        # child count: uniform between ceil(rate - 1.5) and ceil(rate + 1.5)
        floor_child_cnt = math.ceil(-1.5 + birth_rate)
        ceiling_child_cnt = math.ceil(1.5 + birth_rate)

        # Citation: https://www.w3schools.com/python/ref_random_randint.asp
        rnd_child_cnt = self.rnd_gen.randint(max(0, floor_child_cnt), ceiling_child_cnt) # need max to prevent negative counts

        # also reduce child count by 1 if they have no spouses (per req)
        if parent1.spouse is None or parent2.spouse is None:
            rnd_child_cnt = max(0, rnd_child_cnt - 1)

        if rnd_child_cnt == 0:
            return

        # distribute birth years evenly from parent_yr+25 to parent_yr+45
        for i in range(rnd_child_cnt):

            # if there will only be 1 child then put it directly between 25 and 45 years old
            if rnd_child_cnt == 1:
                birth_year = parent1.yr_born + 35
            else:
                # else split them up evenly between 25 and 45
                birth_offset = round(i * 20 / (rnd_child_cnt - 1))
                birth_year = parent1.yr_born + 25 + birth_offset

            # stop if child would be born after max year
            if birth_year > self.MAX_YEAR:
                return

            # create child person object given params
            # then add to tree and allow build to continue
            new_child = self.person_factory.build_person(
                PersonType.CHILD,
                parent1=parent1,
                parent2=parent2,
                birth_year=birth_year
            )

            # add child to both parents' list of children
            parent1.children.append(new_child)

            # add to parent 2 as well if they are not the same
            if parent2 is not parent1:
                parent2.children.append(new_child)

            # update tree for future building
            self.tree.add_people(new_child)

            # give child a spouse based on marriage rate
            dec_new_child = f"{birth_year - (birth_year % 10)}s"
            new_child_mar_rate = self.input_data.marriage_rate_data.get(dec_new_child, self.DEF_MAR_RATE)

            # play some chance to determine if this child gets married
            if new_child_mar_rate > self.rnd_gen.random():
                new_child_spouse = self.person_factory.build_person(PersonType.SPOUSE, person=new_child)

                # update tree for child's spouse
                self.tree.add_people(new_child_spouse)

                # update spousal situation
                new_child.spouse = new_child_spouse
                new_child_spouse.spouse = new_child

                # rebuild children
                self.build_children(new_child, new_child_spouse)
            else:
                # still allow the child to become a single parent, just make sure that there are 1 less children
                # also, neeed a guard to prevent infinite loop on tree additions
                self.build_children(new_child, new_child)
