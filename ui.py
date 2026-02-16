


class FamilyTreeManagerUi:


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
                    print('XXX')
                elif user_input == 'N':
                    print('There are XXX duplicate names in the tree:')
                else:
                    print('Invalid input')

            except Exception as e:
                print(f"ERROR: {e}")


    def get_total(self):
        """Get total number of people in the tree"""
        return len(ft.people)


    def get_decade_people(self):
        pass


    def get_duplicates(self):
        pass

