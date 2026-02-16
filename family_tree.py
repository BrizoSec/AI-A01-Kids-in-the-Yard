class FamilyTree:
    def __init__(self):
        """Init an empty family tree with no people or roots."""
        self.people = []
        self.roots = []

    def add_person(self, person):
        """Add person to the family tree."""
        self.people.append(person)

    def get_people(self):
        """return the list of all people in the family tree."""
        return self.people

    def get_root(self):
        """return the list of root ancestors in the family tree."""
        return self.roots

    def add_root(self, root):
        """Add root to the family tree."""
        self.roots.append(root)
        self.people.append(root)
