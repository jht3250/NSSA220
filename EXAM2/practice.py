import os
import sys

def read_data(file):
    txt = open(file, 'r')
    return txt

def clean(ls):
    arr = []
    for line in ls:
        lin = line.strip()
        lin = lin.split(',')
        lin = [float(i) for i in lin]
        arr.append(lin)
    return arr

def compute_smallest_addition(C, D):
    index = 0
    sm = 0
    diff = 0
    arr = []
    i = 0
    for coord in C:
        diff = abs(coord[0] - D[0][0])
        index = 0
        i = 0
        for coord2 in D:
            currDiff = abs(coord[0] - coord2[0])
            if (currDiff <= diff):
                diff = currDiff
                sm = coord[0] + coord2[0]
                index = i
            i += 1
        arr.append((round(sm, 2), index))
    for i, v in enumerate(arr):
        print(f"The smallest addition of the X position of point C[{i}] ({C[i]}) is D[{v[1]}] ({D[v[1]]}). Addition = {v[0]}")
    return arr

def main():
    txt1 = clean(read_data(sys.argv[1]))
    txt2 = clean(read_data(sys.argv[2]))
    compute_smallest_addition(txt1, txt2)
    


if __name__ == "__main__":
    main()
