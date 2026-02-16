
class FamilyTree:
    def __init__(self):
        self.people = []
        self.root = []

    def add_person(self, person):
        self.people.append(person)

    def get_people(self):
        return self.people

    def get_root(self):
        return self.root

    def set_root(self, root):
        self.root = root

    # get total count

