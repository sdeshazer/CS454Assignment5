# ! /usr/bin/python3

import sys


def read_input():
    for line in sys.stdin:
        line = line.strip()
        data = line.split()

        if data[-1] == 'T':
            print('%s\t%s\t%s' % (data[0], data[1], data[2]))


if __name__ == '__main__':
    read_input()
