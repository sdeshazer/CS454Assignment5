#! /usr/bin/python3
# Samantha Deshazer

import sys


def reducer():
    currentSize = 0
    currentVisits = 0
    currentPage = None
    page = None

    for line in sys.stdin:
        line = line.strip()
        # we only care about the true pages:
        page, numOfVisits, size = line.split('\t')

        try:
            numOfVisits = int(numOfVisits)
        except ValueError:
            continue
        try:
            size = int(size)
        except ValueError:
            continue

        if currentPage == page:
            currentVisits += numOfVisits
            currentSize += size

        else:
            # log to standard out
            if currentPage:
                print(str(currentPage) + " {visits} " + str(currentVisits))
                print(str(currentPage) + " {size} " + str(currentSize))

            currentPage = page
            currentVisits = numOfVisits
            currentSize = size

    if currentPage == page:
        print(str(currentPage) + " {visits} " + str(currentVisits))
        print(str(currentPage) + " {size} " + str(currentSize))


if __name__ == '__main__':
    reducer()
