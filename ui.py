


class FamilyTreeManagerUi:

    def __init__(self, ft):
        self.family_tree = ft


    def start(self):
        while True:
            # print('Starting Family Tree Generator UI')

            # using example values from documentation
            print('(T)otal number of people in the tree')
            print('Total number of people in the tree by (D)ecade')
            print('(N)ames duplicated')
            # print('\n')

            try:
                user_input = input('> ').strip()
                print(user_input)

            except Exception as e:
                print(e)
