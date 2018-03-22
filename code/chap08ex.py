from estimation import RMSE, MeanError
import random
import matplotlib.pyplot as plt
import numpy as np
import thinkplot
import thinkstats2


def simulate_game(goals_per_game=1.0):
    num_goals = 0
    time = 0
    while True:
        time_btw_goals = random.expovariate(goals_per_game)
        time += time_btw_goals
        if time > 1:
            break
        num_goals += 1
    return num_goals


def exercise_8_3():
    lam = 2
    estimates = []
    for _ in range(100):
        L = simulate_game(lam)
        estimates.append(L)

    print('rmse L', RMSE(estimates, lam))
    print('mean error L', MeanError(estimates, lam))

    pmf = thinkstats2.Pmf(estimates)
    thinkplot.Hist(pmf)
    thinkplot.Config(xlabel='Goals scored', ylabel='PMF')
    thinkplot.Show()


def exercise_8_2_multi_n():
    """
    Demonstrates how standard error decreases as sample size increases
    """
    ns = np.linspace(10, 1000, 100, dtype=int)
    lambd = 2
    m = 1000

    stderrs = []
    for n in ns:
        estimates = []
        for _ in range(m):
            sample = np.random.exponential(1.0 / lambd, n)
            L = 1 / np.mean(sample)
            estimates.append(L)
        stderr = RMSE(estimates, lambd)
        stderrs.append(stderr)

    plt.plot(ns, stderrs)
    plt.xlabel('Sample size')
    plt.ylabel('Standard error')
    plt.show()


def exercise_8_2():
    n = 10
    lambd = 2
    m = 1000

    estimates = []
    for _ in range(m):
        sample = np.random.exponential(1.0 / lambd, n)
        L = 1 / np.mean(sample)
        estimates.append(L)

    stderr = RMSE(estimates, lambd)
    cdf = thinkstats2.Cdf(estimates)

    print('Exercise 8.2')
    print('Standard error: ', stderr)
    print('90%% confidence interval: %s ~ %s' % (cdf.Percentile(5), cdf.Percentile(95)))

    thinkplot.Cdf(cdf)
    thinkplot.Show()


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
    exercise_8_3()


if __name__ == '__main__':
    main()
