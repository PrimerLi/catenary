import os
import sys

def readParameters():
    my_file1 = 'parameters.txt'
    if (not os.path.exists(my_file1)):
        print my_file1 + ' does not exist!'
        sys.exit(-1)
    ifile = open(my_file1, 'r')
    strings = ifile.readlines()
    ifile.close()
    a = float(strings[0].split(" = ")[1])
    Delta = float(strings[1].split(" = ")[1])
    N = int(strings[2].split(" = ")[1])
    if N * Delta <= a:
        print "Make sure that N * Delta > a. "
        sys.exit(-1)
    return a, Delta, N

def main():
    readParameters()

if __name__ == "__main__":
    import sys
    sys.exit(main())
