import matplotlib.pyplot as plt
import numpy as np

# Read data from iris.csv
def read_data(filename):
    with open(filename, 'r') as file:
        data = [list(map(float, line.strip().split(','))) for line in file]
    return data

# Process data
filename = 'iris.csv'
data = read_data(filename)
setosa, versicolor, virginica = [], [], []

for record in data:
    if record[4] == 1.0:
        setosa.append(record)
    elif record[4] == 2.0:
        versicolor.append(record)
    elif record[4] == 3.0:
        virginica.append(record)

setosa_arr = np.array(setosa)
versicolor_arr = np.array(versicolor)
virginica_arr = np.array(virginica)

# Create a line plot for petal length of each iris type
plt.plot(setosa_arr[:, 2], color='black', label='Setosa')
plt.plot(versicolor_arr[:, 2], color='red', label='Versicolor')
plt.plot(virginica_arr[:, 2], color='blue', label='Virginica')
plt.legend(loc='upper right')
plt.title('Petal Length of Each Iris Type')
plt.xlabel('Instance Number')
plt.ylabel('Petal Length (cm)')
plt.savefig('petal_length_line_plot.png')
plt.close()

# Create a scatter plot for sepal length vs sepal width
plt.scatter(setosa_arr[:, 0], setosa_arr[:, 1], color='black', marker='*', label='Setosa')
plt.scatter(versicolor_arr[:, 0], versicolor_arr[:, 1], color='red', marker='+', label='Versicolor')
plt.scatter(virginica_arr[:, 0], virginica_arr[:, 1], color='blue', marker='o', label='Virginica')
plt.legend(loc='upper right')
plt.title('Sepal Length vs Sepal Width')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.xlim(4, 8)  # Adjust x-axis limits
plt.ylim(2, 5)  # Adjust y-axis limits
plt.savefig('sepal_scatter_plot.png')
plt.close()
