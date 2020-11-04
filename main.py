# coding=utf-8
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import sys, getopt

from model import constants
from readerFile.fileReader import FileReader
from reductor.reductor import Reductor

def main(name, argv):
    # Use a breakpoint in the code line below to debug your script.
    print("SAT To X-SAT, {0}".format(name))  # Press Ctrl+F8 to toggle the breakpoint.
    try:
        opts, args = getopt.getopt(argv, "x", ["inumber="])
        for opt, arg in opts:
            if opt == '-x' and (len(args) == 0 or args[0] < 3 or args[0] == '') :
                print ("Please insert your arguments")
                sys.exit()
            elif opt == '-x' and len(args) > 0 and args[0] != '':
                print ("Right-reading")
                procedure(int(args[0]))
            else:
                print ("Processing error")
                pass

    except getopt.GetoptError:
        print ('Error at main.py -x <inputnumber>')
        sys.exit(2)


def procedure(x_sat):

    # Define FileReader and create clause structure
    for filename in os.listdir(constants.DIR_READ_LINUX):
        print('filename >>>> '  + filename)
        fileReader = FileReader(os.path.join(constants.DIR_READ_LINUX, filename))
        fileReader.read_file()

        # print(fileReader.get_listClauses())

        # Define solver
        reductor = Reductor(x_sat, fileReader.get_numLiterals())
        reductor.transform_sat_to_3sat(fileReader.get_listClauses())
        reductor.transform_3sat_to_xsat()
        reductor.write_dimacs_file(filename)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('Start', sys.argv[1:])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
