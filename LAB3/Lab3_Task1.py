import sys
import math

def read_data(filename, records):
    with open(filename, 'r') as f:
        lines = f.readlines()
        ready = False
        for line in lines:
            if line.strip() == "@DATA":
                ready = True
                continue
            if ready:
                records.append(line.strip().split(","))

def process_numeric_field(records, field_index):
    values = [float(record[field_index]) for record in records]
    min_val = min(values)
    max_val = max(values)
    avg_val = round((sum(values) / len(values)), 2)
    std_dev = round((math.sqrt(sum((x - avg_val) ** 2 for x in values) / len(values))), 2)  #calculate standard deviation
    return min_val, max_val, avg_val, std_dev

def count_iris_types(records):
    iris_counts = {"Iris-setosa": 0, "Iris-versicolor": 0, "Iris-virginica": 0}
    for record in records:
        iris_counts[record[-1]] += 1
    return iris_counts["Iris-setosa"], iris_counts["Iris-versicolor"], iris_counts["Iris-virginica"]

if __name__ == "__main__":
    records = []
    read_data(sys.argv[1], records)

    fields = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width"]
    for i in range(len(fields)):
        min_val, max_val, avg_val, std_dev = process_numeric_field(records, i)
        print(fields[i], ": min = ", min_val, ", max = ", max_val, ", average = ", avg_val, ", standard deviation = ", std_dev, sep="")

    setosa_count, versicolor_count, virginica_count = count_iris_types(records)
    print(f"Iris Types: Iris Setosa = {setosa_count}, Iris Versicolor = {versicolor_count}, Iris Virginica = {virginica_count}")


