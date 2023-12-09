import csv

from statzcw import z_count, z_mean, z_variance, z_corr, z_median, z_mode, z_stddev, z_stderr


# Create a function to read the data from a CSV and return a dictionary with 'X' and 'Y' lists
def read_csv(file_path):
    data = {'X': [], 'Y': []}
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data['X'].append(float(row['X']))
            data['Y'].append(float(row['Y']))
    return data


# Create a function to print various stats fo9r a given a data set
def print_statistics(data, index):
    x_data = data['X']
    y_data = data['Y']

    print(f"Data Set {index}:")
    print(f"Count of X: {z_count(x_data)}")
    print(f"Count of Y: {z_count(y_data)}")
    print(f"Mean of X: {z_mean(x_data)}")
    print(f"Sample Variance of X: {z_variance(x_data)}")
    print(f"Mean of Y: {z_mean(y_data)}")
    print(f"Sample Variance of Y: {z_variance(y_data)}")
    print(f"Correlation between X and Y: {z_corr(x_data, y_data)}")
    print(f"Median of X: {z_median(x_data)}")
    print(f"Median of Y: {z_median(y_data)}")
    print(f"Mode of X: {z_mode(x_data)}")
    print(f"Mode of Y: {z_mode(y_data)}")
    print(f"Sample Std deviation of X: {z_stddev(x_data)}")
    print(f"Sample Std Deviation of Y: {z_stddev(y_data)}")
    print(f"Standard Error of the Mean of X: {z_stderr(x_data)}")
    print(f"Standard Error of the Mean of Y: {z_stderr(y_data)}")
    print("\n")


# Read and print stats for each data set
for i in range(4):
    file_path = f"data{i}.csv"
    data = read_csv(file_path)
    print_statistics(data, i)
