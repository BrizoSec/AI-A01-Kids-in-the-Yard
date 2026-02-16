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
        """create child person"""

        _gender = gender_picker(self.input_data.gender_prob_data, f"{birth_year - (birth_year % 10)}s")
        # _f_name =


    def build_spouse(self, person: Person):
        pass


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
