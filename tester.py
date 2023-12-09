from statzcw import z_count, z_mean, z_median, z_mode, z_variance, z_stddev, z_stderr, z_corr

print(z_count([1, 2, 3, 4, 5]))

print(z_mean([1, 2, 3, 4, 5]))

print(z_mode([1, 2, 2, 3, 4, 4, 4, 5,]))

print(z_median([1.0, 2.0, 2.0, 4.0, 5.0]))

print(z_variance([1, 2, 3, 4, 5]))

print(z_stddev([1, 2, 3, 4, 5]))

print(z_stderr([1, 2, 3, 4, 5]))

print(z_corr([1, 2, 3, 4, 5], [2, 3, 4, 5, 6]))

