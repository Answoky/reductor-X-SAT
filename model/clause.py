
class Clause():

    #listLiterals

    def __init__(self):
        self.listLiterals = []

    # Get and Set

    def add_listLiterals(self, literal):
        self.listLiterals.append(literal)

    def add_list_to_listLiterals(self, list):
        for literal in list.split()[:-1]:
            self.listLiterals.append(int(literal))

    def pop_listLiterals_position(self, position):
        return self.listLiterals.pop(position)

    def get_listLiterals(self):
        return self.listLiterals

    def get_listLiterals_position(self, position):
        return self.listLiterals[position]

    def set_listLiterals(self, list_literals):
        self.listLiterals = list_literals[:]