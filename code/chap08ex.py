from estimation import RMSE, MeanError
import random
import matplotlib.pyplot as plt
import numpy as np


def exercise_8_1():
    # as the sample size increases, the root mean squared error decreases
    # the bigger the sample size, the more accurate the estimation
    sample_size = 10
    number_of_iter = 1000

    mu = 0
    stdev = 1
    var = stdev ** 2

    means = []
    medians = []

    estimates1 = []
    estimates2 = []

    for _ in range(number_of_iter):
        sample = np.random.normal(mu, stdev, sample_size)

        xbar = np.mean(sample)
        median = np.median(sample)
        means.append(xbar)
        medians.append(median)

        var_biased = np.var(sample)
        var_unbiased = np.var(sample, ddof=1)
        estimates1.append(var_biased)
        estimates2.append(var_unbiased)

    print('Exercise 8.1')
    print('RMSE xbar', RMSE(means, mu))  # yields lower RMSE than median
    print('RMSE median', RMSE(medians, mu))
    print('RMSE var biased', RMSE(estimates1, var))  # yields lower RMSE than biased var
    print('RMSE var unbiased', RMSE(estimates2, var))


def main():
    exercise_8_1()


if __name__ == '__main__':
    main()
