# John Treon NSSA 220 Exam 2 04/11/2025 (Taken at the DSO Testing Center)
# usage: python3 exam2.py [file1] [file2]
# This python script calculates the Euclidian Distance between two points in file1 and file2, and 
# finds the closest point (smallest Euclidian Distance) for each point in file1 against all in file2

import os
import sys

# reads in the data, and calls the clean method to return a properly formatted array
# param: file -> array
# returns: the usable array 
def read_data(file):
    txt = open(file, 'r')
    txt = clean(txt)
    return txt

# takes in a string array (lines in a file) and iterates line by line, removing whitespace and newlines, and splitting 
# param: ls -> the array to be formatted
# returns: the formatted array
def clean(ls):
    arr = []
    for line in ls: 
        lin = line.strip()
        lin = lin.split(',')
        lin = [float(i) for i in lin] # cast each item in the line to a float
        arr.append(lin)
    return arr

# computes the shortest distance for each point in A to a point in B. Calculated using the Euclidian Distance formula,
# (distance = sqrt((x2 - x1)^2 + (y2 - y1)^2). Prints each pair of coordinates and their distance.
# param: A -> the first array of coordinates, B -> the second array of coordinates
# returns: nothing
def compute_distance(A, B):
    index = 0
    dis = 0
    arr = []
    i = 0
    for coord in A:
        dis = (((B[0][0] - coord[0]) ** 2) + ((B[0][1] - coord[1]) ** 2)) ** 0.5 # initialize with the first value that will be computed anyways
        index = 0
        i = 0
        for coord2 in B:
            x1 = coord[0]
            y1 = coord[1]
            x2 = coord2[0]
            y2 = coord2[1]
            currDis = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5 # euclidian distance formula
            if (currDis <= dis):
                dis = currDis
                index = i
            i += 1
        arr.append((round(dis, 3), index))
    for i, v in enumerate(arr):
        print(f"The closest point to A[{i}] is point B[{v[1]}]. Distance = {v[0]}")


def main():
    inp1 = read_data(sys.argv[1])
    inp2 = read_data(sys.argv[2])
    compute_distance(inp1, inp2)

if __name__ == "__main__":
    main()
