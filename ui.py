


class FamilyTreeManagerUi:
    """Family Tree Manager UI Class"""

    def print_duplicate_full_names(self):
        """Get duplicate first + last name combinations"""
        _name_cnt = {}

        # get entire name and check if it exists
        for p in self.family_tree.people:
            name = p.get_entire_name()

            if name not in _name_cnt:
                _name_cnt[name] = 0

            # increment by 1 for new detection
            _name_cnt[name] += 1

        # initialize duplicates list
        duplicates = []
        for name, count in _name_cnt.items():
            if count > 1:
                duplicates.append(name)

        # evaluate and display results
        if not duplicates:
            print("No duplicate names")

        else:
            # print number and loop over to show who they are
            print(f"\nThere are {len(duplicates)} duplicate names in the tree: ")
            for name in duplicates:
                print(f"* {name}")


    def __init__(self, ft):
        self.family_tree = ft


    def start(self):
        """Start the interactive UI."""

        while True:
            # print('Starting Family Tree Generator UI')

            # using example values from documentation
            print('(T)otal number of people in the tree')
            print('Total number of people in the tree by (D)ecade')
            print('(N)ames duplicated')
            # print('\n')

            try:
                user_input = input('> ').strip()
                # print(user_input)

                if user_input == 'T':
                    print(f'The tree contains {self.get_total()} people total')
                elif user_input == 'D':
                    self.print_decades_with_counts()
                elif user_input == 'N':
                    self.print_duplicate_full_names()
                else:
                    print('Invalid input')

            except Exception as e:
                print(f"ERROR: {e}")


    def get_total(self):
        """Get total number of people in the tree"""
        return len(self.family_tree.people)


    def print_decades_with_counts(self):
        _dec = {}

        for p in self.family_tree.people:
            decade = p.get_born_decade()

            # init if not existing
            if decade not in _dec:
                _dec[decade] = 0

            # increment by 1 for new detection
            _dec[decade] += 1

            # sort decades
            decades_sorted = sorted(_dec.items(), key=lambda x: x[0])

            # print each item in decades which is now sorted
            for decade, count in decades_sorted.items():
                print(f"{decade}: {count}")
