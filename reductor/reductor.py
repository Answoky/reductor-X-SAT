# -*- coding: utf-8 -*-

from model import constants
from model.clause import Clause

class Reductor():

    def __init__(self, x_sat, number_literals):
        self.x_sat = x_sat
        self.total_number_literals = int(number_literals)
        self.new_number_literals = 0
        self.list_clause_3sat = []
        self.list_ilution = []
        self.final_list_clause_xsat = []

    # Transform SAT to 3SAT
    def transform_sat_to_3sat(self, list_clause):
        for clause in list_clause:
            k = len(clause)
            if k == 1:
                self.equal_one(clause)
            if k == 2:
                self.equal_two(clause)
            if k == 3:
                self.equal_three(clause)
            if k > 3:
                self.more_than_three(clause)
        # self.to_string(self.list_clause_3sat)

    # Principal funtions

    def equal_one(self, clause):
        # print ("First Case")
        new_literals = self.create_literals(constants.CREATE_TWO_LITERAL)
        self.add_literal_to_new_clauses(clause, new_literals)
        pass

    def equal_two(self, clause):
        # print ("Second Case")
        new_literals = self.create_literals(constants.CREATE_ONE_LITERAL)
        self.add_literal_to_new_clauses(clause, new_literals, self.list_clause_3sat)

    def equal_three(self, clause):
        # print ("Third Case")
        new_clause = Clause()
        new_clause.set_listLiterals(clause)
        self.list_clause_3sat.append(new_clause)

    def more_than_three(self, clause):
        # print ("Four Case")
        k = len(clause)
        new_literals = self.create_literals((k - constants.THREE) )
        self.add_clauses_for_more_than_three(clause, new_literals, (k - constants.TWO) )

    # Creation literals and clauses

    def create_literals(self, amount_literal_create):
        new_list_literals = []
        for i in range(1, (amount_literal_create + constants.ONE)):
            self.new_number_literals += 1
            self.total_number_literals += 1
            new_list_literals.append(self.total_number_literals)
            new_list_literals.append("-" + str(self.total_number_literals))
        return new_list_literals

    def add_literal_to_new_clauses(self, clause, new_literals, list_to_add):
        for literal in new_literals:
            new_clause = Clause()
            new_clause.set_listLiterals(clause)
            new_clause.add_listLiterals(literal)
            list_to_add.append(new_clause)

    def add_clauses_for_more_than_three(self, clause, new_literals, size):
        for x in range(1, (size+1)):
            if x == 1:
                self.list_clause_3sat.append(self.create_first_clause(clause, new_literals))
            elif x >= 2 and x < size :
                self.list_clause_3sat.append(self.create_rest_of_clauses(clause, new_literals))
            elif x == size:
                self.list_clause_3sat.append(self.create_last_clause(clause, new_literals))
            else:
                pass

    # You can create the first clause with format ( z1 ∨ z2 ∨ v1 )
    def create_first_clause(self, clause, new_literals):
        new_clause = Clause()
        new_clause.add_listLiterals(clause.pop(0))
        new_clause.add_listLiterals(clause.pop(0))
        new_clause.add_listLiterals(new_literals.pop(0))
        return new_clause

    # You can create the second clause and the rest of clauses with format ( ¬v1 ∨ z3 ∨ v2 )
    def create_rest_of_clauses(self, clause, new_literals):
        new_clause = Clause()
        new_clause.add_listLiterals(new_literals.pop(0))
        new_clause.add_listLiterals(clause.pop(0))
        new_clause.add_listLiterals(new_literals.pop(0))
        return new_clause

    # You can create the last clause with format ( ¬vk−3 ∨ zk−1 ∨ zk )
    def create_last_clause(self, clause, new_literals):
        new_clause = Clause()
        new_clause.add_listLiterals(new_literals.pop(0))
        new_clause.add_listLiterals(clause.pop(0))
        new_clause.add_listLiterals(clause.pop(0))
        return new_clause

    # Transform 3SAT TO X-SAT
    def transform_3sat_to_xsat(self):
        for x in range(0, (self.x_sat - constants.THREE) ):
            if x == 0:
                self.final_list_clause_xsat = self.iteration_list( self.list_clause_3sat)
            elif x > 0:
                self.final_list_clause_xsat = self.iteration_list( self.final_list_clause_xsat)
            else:
                pass

        # print (self.get_new_number_literals())
        # self.to_string (self.final_list_clause_xsat)

    def iteration_list(self, lis_to_iterate):
        self.list_ilution = []
        for clause in lis_to_iterate:
            new_literals = self.create_literals(constants.CREATE_ONE_LITERAL)
            self.add_literal_to_new_clauses(clause.get_listLiterals(), new_literals, self.list_ilution)
        return self.list_ilution[:]

    def write_dimacs_file(self, file_name):
        path = constants.DIR_WRITE_LINUX + file_name
        f = open(path, 'wb')
        f.write("c ================================================\n")
        f.write("c \n")
        f.write("c Archivo convertido a " + str(self.x_sat) + "-SAT" + "\n")
        f.write("c Nombre " + file_name + "\n")
        f.write("c \n")
        f.write("c ================================================\n")
        f.write("p cnf " + str(self.get_total_number_literals()) + " " + str(len(self.get_final_list_clause_xsat())) + "\n" )
        f.write(self.to_string_print (self.final_list_clause_xsat))
        f.close()

    def is_clause_3sat(self, clause_3sat):
        return len(clause_3sat) == 3


    # Get and Set

    def add_clause_3sat(self, clause):
        self.list_clause_3sat.append(clause)

    def add_list_clause_3sat(self, list_clause):
        for literal in list_clause.split()[:-1]:
            self.list_clause_3sat.append(int(literal))

    def get_list_clause_3sat(self):
        return self.list_clause_3sat

    def get_list_clause_3sat_position(self, position):
        return self.list_clause_3sat[position]

    def set_list_clause_3sat(self, list_clause):
        self.list_clause_3sat = list_clause[:]

    def get_final_list_clause_xsat(self):
        return self.final_list_clause_xsat

    def get_final_list_clause_xsat_position(self, position):
        return self.final_list_clause_xsat[position]

    def set_final_list_clause_xsat(self, list_clause):
        self.final_list_clause_xsat = list_clause[:]

    def get_x_sat(self):
        return self.x_sat

    def set_x_sat(self, x_sat):
        self.x_sat = x_sat

    def get_new_number_literals(self):
        return self.new_number_literals

    def set_new_number_literals(self, new_number_literals):
        self.new_number_literals = new_number_literals

    def get_total_number_literals(self):
        return self.total_number_literals

    def set_total_number_literals(self, total_number_literals):
        self.total_number_literals = total_number_literals

    def to_string(self, list_clause):
        for clause in list_clause:
            print (clause.get_listLiterals())

    def to_string_print(self, list_clause):
        clause_list = ""
        for clause in list_clause:
            clause_list += ' '.join(map(str,clause.get_listLiterals())) + ' 0 ' + "\n"
        return clause_list