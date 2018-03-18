# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

import analytic
import thinkstats2
import thinkplot
import nsfg


def exponential_distribution(x, _lambda=1.0):
    return 1 - np.exp(-_lambda * x)


def exponential_distribution_plot():
    x = np.arange(0, 5, 0.1)
    y1 = exponential_distribution(x, 0.5)
    y2 = exponential_distribution(x, 1.0)
    y3 = exponential_distribution(x, 2.0)
    plt.plot(x, y1, color='blue', label='λ=0.5')
    plt.plot(x, y2, color='green', label='λ=1.0')
    plt.plot(x, y3, color='orange', label='λ=2.0')
    plt.legend()
    plt.show()


def visualize_normal_cdf():
    x = np.arange(-3, 4, 0.1)
    y1 = scipy.stats.norm.cdf(x, loc=0, scale=1.0)
    y2 = scipy.stats.norm.cdf(x, loc=1, scale=0.5)
    y3 = scipy.stats.norm.cdf(x, loc=2, scale=0.4)
    y4 = scipy.stats.norm.cdf(x, loc=3, scale=0.3)
    plt.title('Normal Distribution CDF')
    plt.plot(x, y1, color='blue', label='mu=0, sig=1.0')
    plt.plot(x, y2, color='orange', label='mu=1, sig=0.5')
    plt.plot(x, y3, color='red', label='mu=2, sig=0.4')
    plt.plot(x, y4, color='green', label='mu=3, sig=0.3')
    plt.legend()
    plt.show()


def totalwgt_lb_dist_visualization():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    cdf = thinkstats2.Cdf(live.totalwgt_lb)

    x = np.arange(0, 15, 0.1)
    y1 = []
    for val in x:
        y1.append(cdf[val])
    plt.title('totalwgt_lb')
    plt.plot(x, y1, label='data')
    plt.plot(x, scipy.stats.norm.cdf(x, loc=7.28, scale=1.24), label='model mu=7.28 sig=1.24')
    plt.legend()
    plt.show()


def feet_inches_to_meters(feet=0, inches=0):
    sum_inches = (feet * 12) + inches
    return (sum_inches / 12) * .3048


def exercise_5_1():
    mu = 178  # mean
    sigma = 7.7  # standard deviation
    dist = scipy.stats.norm(loc=mu, scale=sigma)  # normal distribution
    h5_10_cm = feet_inches_to_meters(5, 10) * 100
    h6_1_cm = feet_inches_to_meters(6, 1) * 100

    low = dist.cdf(h5_10_cm)
    high = dist.cdf(h6_1_cm)

    print(low, high, high - low)  # 0.489639027865 0.832385865496 0.342746837631


def main():
    exercise_5_1()


if __name__ == '__main__':
    main()
