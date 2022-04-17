#! /usr/bin/python3
import sys


def reducer():
    currentSize = 0
    currentVisits = 0
    currentPage = None
    page = None

    for line in sys.stdin:
        line = line.strip()
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
            if currentPage:
                print(currentPage + " {visits} " + currentVisits)
                print(currentPage + " {size} " + currentSize)
            currentPage = page
            currentVisits = numOfVisits
            currentSize = size

    if currentPage == page:
        print(currentPage + " {visits} " + currentVisits)
        print(currentPage + " {size} " + currentSize)


if __name__ == '__main__':
    reducer()
