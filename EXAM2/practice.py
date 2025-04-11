import os
import sys

ctxt = open("C.txt", 'r')
dtxt = open("D.txt", 'r')

def read_data(file):
    txt = open(file, 'r')
    for line in txt:
        print(line)

def main():
    read_data(sys.argv[1])
    read_data(sys.argv[2])

if __name__ == "__main__":
    main()

