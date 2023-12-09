import math


def z_count(lis: list) -> float:
    # Count the number in the elements in the list
    count = len(lis)
    return count


def z_mean(lis: list) -> float:
    # Calculate the mean by summing the numbers in the list and dividing by the list's count (number of values in the
    # list(length))
    mean = sum(lis) / len(lis)
    return mean


def z_mode(lis: list) -> float:
    # Create a dictionary to store the occurrence of each number
    dict = {}
    for num in lis:
        # Use get to retrieve the current occurrence  or default to 0, then increment
        dict[num] = dict.get(num, 0) + 1

    # Find the mode(s)
    # Identify keys (numbers) with the maximum occurrence
    modes = [key for key, value in dict.items() if value == max(dict.values())]

    # If there is more than one mode, return the first one
    # Otherwise, return None if there are no modes
    return modes[0] if len(modes) > 0 else None


def z_median(lis: list) -> float:
    mid = len(lis) // 2
    return lis[mid]


def z_variance(lis: list) -> float:
    # Variance measures how far a data set is spread out. It is mathematically defined as the average of the squared
    # differences from the mean. Then calculate the mean
    mean = sum(lis) / len(lis)

    # Calculate the squared difference from mean
    squared_diff = [(x - mean) ** 2 for x in lis]

    # The variance is the average of squared differences from the mean. Calculate it
    variance = sum(squared_diff) / len(lis)

    return variance


def z_stddev(lis: list) -> float:
    # Standard deviation is just the square root of the variance of a list
    # Calculate the variance using z_variance function
    variance = z_variance(lis)

    # Standard deviation is the square root of the variance, now calculate it
    stddev = math.sqrt(variance)

    return stddev


def z_stderr(lis: list) -> float:
    # Standard Error is simply the standard deviation divided by the square root of the count
    # Calculate the standard deviation using the zstddev function
    stddev = z_stddev(lis)

    # Calculate the standard error of mean
    stderr = stddev / math.sqrt(len(lis))

    return stderr


def z_corr(listx: list, listy: list) -> float:
    # Figure out the _covariance_ between the two lists.
    # Then the correlation is the covariance divided by the stddev of each list multiplied together
    # Calculate the mean of x and y
    mean_x = sum(listx) / len(listx)
    mean_y = sum(listy) / len(listy)

    # Calculate the covariance
    # Standard deviation is a measure of the amount of variation in a set of values
    covariance = sum((x - mean_x) * (y - mean_y) for x, y in zip(listx, listy)) / len(listx)

    # Calculate the standard deviations
    stddev_x = z_stddev(listx)
    stddev_y = z_stddev(listy)

    # Calculate the correlation coefficient
    # Correlation coefficient is the normalized measure of the strength and direction of a linear relationship between two variables
    correlation = covariance / (stddev_x * stddev_y)

    return correlation


def cov(a, b):
    if z_count(a) != z_count(b):
        raise ValueError("The length of 'a' and 'b' must be equal.")

    sum = 0
    for i in range(z_count(a)):
        sum += (a[i] - z_mean(a)) * (b[i] - z_mean(b))

    covariance = sum / (z_count(a) - 1)
    return covariance
