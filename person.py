from dataclasses import dataclass, field


@dataclass
class Person:
    """Person in family tree class"""

    uid: int
    f_name: str
    l_name: str
    gender: str
    parent1 = None
    parent2 = None
    spouse = None
    generation_rank = int
    yr_married: int
    yr_deceased: int
    children: list = field(default_factory=list)
    yr_born: int = None


    def get_entire_name(self):
        "get full name"
        return f"{self.f_name} {self.l_name}"


    def get_born_decade(self) -> str:
        """Get the decade of birth"""
        return f"{self.yr_born - (self.yr_born % 10)}" # ex: 1956 - 6 = 1950


    # def get_deceased_decade(self):
    #     pass


    def get_is_child_rearing(self, yr):
        current_age = year - self.yr_born

        # if they are a living person between 25 and 40 then yes
        if get_is_alive(yr) and 25 <= current_age <= 45:
            return True

        # else no
        return False



    def get_is_currently_alive(self, year):
        """Return if individual is still alive"""

        # person is not alive if they were not yet born
        if self.yr_born > year:
            return False

        # person is alive if they never died and were born
        if self.yr_deceased is None:
            return True

        # person is dead if they died in a prior year and were born
        if self.yr_deceased < year:
            return False

        # otherwise, they are alive still...
        return True

