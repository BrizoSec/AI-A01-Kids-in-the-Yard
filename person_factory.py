from enum import Enum
from helper_utils import gender_picker, f_name_picker, l_name_picker, deceased_year_picker
from person import Person
import random


class PersonType(Enum):
    """Enum representing the type of person to build"""
    SPOUSE = "spouse"
    ROOT = "root"
    CHILD = "child"


class PersonFactory:
    """factory to build persons w/ acceptable params per document"""

    def __init__(self, rnd_gen=None, input_data=None):
        self.rnd_gen = rnd_gen if rnd_gen else random.Random()
        self.input_data = input_data
        self.uid = 0
        self.generation_rank = 1


    def build_person(self, person_type: PersonType, **person_params):
        """Build and return a person of the given type using the provided kwargs."""

        # build root if root
        if person_type == PersonType.ROOT:
            return self.build_root_person()

        # child if child
        elif person_type == PersonType.CHILD:
            return self.build_child(
                person_params['parent1'],
                person_params['parent2'],
                person_params['birth_year']
            )

        # spouse if spouse
        elif person_type == PersonType.SPOUSE:
            return self.build_spouse(person_params['person'])

        # throw error otherwise
        else:
            raise ValueError(f"Unknown person type: {person_type}")


    def build_child(self, parent1, parent2, birth_year):
        """Build a child person from two parents."""
        decade = f"{birth_year - (birth_year % 10)}s"
        gender = gender_picker(self.input_data.gender_prob_data, decade)

        # get first naame and died year
        f_name = f_name_picker(self.input_data.first_name_data, self.input_data.gender_prob_data, decade)
        yr_deceased = deceased_year_picker(self.input_data.life_exp_data, birth_year)

        # inherit a parent's last name if either parent is a root of the tree
        if parent1.generation_rank == 1 or parent2.generation_rank == 1:
            # Citation: https://docs.python.org/3/library/random.html#random.choice
            l_name = random.choice([parent2.l_name, parent1.l_name])

        # otherwise, just pick from last name list and use rank weights - kind of weird logic
        else:
            l_name = l_name_picker(self.input_data.last_name_data, self.input_data.rank_prob_data, decade)

        self.uid += 1

        return Person(
            uid=self.uid,
            f_name=f_name,
            l_name=l_name,
            gender=gender,
            yr_deceased=yr_deceased,
            yr_born=birth_year,
            generation_rank=parent1.generation_rank + 1)


    def build_spouse(self, person: Person):
        """Create partner / spouse """
        # first get the decade of the spouse using the +/- 10 rule
        offset_yr = self.rnd_gen.randint(-10, 10)

        # seeing an issue for root people, their parents have NA's in the name so going to limit it to the lowest
        # date in the dataset
        # Citation: https://docs.python.org/3/reference/expressions.html#generator-expressions
        minium_dataset_yr = min(int(d[:-1]) for _, d in self.input_data.first_name_data.keys()) # get min year from decades in dataset
        maximum_dataset_yr = max(int(d[:-1]) for _, d in self.input_data.first_name_data.keys()) # get max year from decades in dataset
        yr_born = max(minium_dataset_yr, min(maximum_dataset_yr, person.yr_born + offset_yr))

        dec = f"{yr_born - (yr_born % 10)}s"

        # then we can calc the gender and so on
        gender = gender_picker(self.input_data.gender_prob_data, dec)
        f_name = f_name_picker(self.input_data.first_name_data, self.input_data.
                               gender_prob_data, dec)
        l_name = l_name_picker(self.input_data.last_name_data, self.input_data.
                               rank_prob_data, dec)
        yr_deceased = deceased_year_picker(self.input_data.life_exp_data, yr_born)

        # increment counter
        self.uid += 1

        return Person(
            uid=self.uid,
            f_name=f_name,
            l_name=l_name,
            gender=gender,
            # yr_married=None,
            yr_deceased=yr_deceased,
            yr_born=yr_born,
            generation_rank=person.generation_rank)


    def build_root_person(self):
        yr_born = 1950
        decade = f"{yr_born - (yr_born % 10)}s" # get decade + s

        # using data passed in
        gender = gender_picker(self.input_data.gender_prob_data, decade)
        f_name = f_name_picker(self.input_data.first_name_data, self.input_data.gender_prob_data, decade)
        l_name = l_name_picker(self.input_data.last_name_data, self.input_data.rank_prob_data, decade)
        yr_deceased = deceased_year_picker(self.input_data.life_exp_data, yr_born)
        
        # increment counter
        self.uid += 1
        
        return Person(
            uid=self.uid,
            f_name=f_name,
            l_name=l_name,
            gender=gender,
            # yr_married=None,
            yr_deceased=yr_deceased,
            yr_born=yr_born)
