
from model.clause import Clause

class FileReader():

    # path
    # listClause
    # type
    # numLiterals
    # numClauses
    # listClauses
    # clause

    def __init__(self, path):
        self.path = path
        self.type = ''
        self.numLiterals = 0
        self.numClauses = 0
        self.listClauses = []
        self.clause = None


    def read_file(self):
        file = open(self.path, "r")
        lines = file.readlines()

        for line in lines:
            # print (line)
            if line[0] == 'c':
                pass
            elif line[0] == 'p':
                self.save_initial_variables(line) # cnf 100 850
            elif line[0] == '%' or line[0] == '%':
                pass
            else:
                self.clause = Clause()
                self.clause.add_list_to_listLiterals(line)
                self.add_clause(self.clause.get_listLiterals())

        # print(self.get_size_listClauses())

    # Funtions to create clause structure

    def save_initial_variables(self,line):
        first_information = line.split()
        self.set_type(first_information[1])
        self.set_numLiterals(first_information[2])
        self.set_numClause(first_information[3])

    def add_clause(self, clause):
        self.listClauses.append(clause)

    # Get and Set

    def get_type(self):
        return self.type

    def set_type(self, type):
        self.type = type

    def get_numLiterals(self):
        return self.numLiterals

    def set_numLiterals(self, numLiterals):
        self.numLiterals = numLiterals

    def get_numClause(self):
        return  self.numClauses

    def set_numClause(self, numClauses):
        self.numClauses = numClauses

    def get_listClauses(self):
        return self.listClauses

    def get_size_listClauses(self):
        return len(self.listClauses)

    def set_listClauses(self, listClauses):
        self.listClauses = listClauses[:]

    def to_string(self):
        print (self.listClauses)