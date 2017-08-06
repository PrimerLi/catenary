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
    a = float(strings[0].split()[2])
    Delta = float(strings[1].split()[2])
    N = int(strings[2].split()[2])
    return a, Delta, N

def main():
    readParameters()

if __name__ == "__main__":
    import sys
    sys.exit(main())
