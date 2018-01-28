import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

import analytic
import thinkstats2
import thinkplot


def exponential_distribution(x, _lambda=1.0):
    return 1 - np.exp(-_lambda * x)


def exponential_distribution_plot():
    x = np.arange(0, 5, 0.1)
    y1 = exponential_distribution(x, 0.5)
    y2 = exponential_distribution(x, 1.0)
    y3 = exponential_distribution(x, 2.0)
    plt.plot(x, y1, color='blue', label='λ = 0.5')
    plt.plot(x, y2, color='green', label='λ = 1.0')
    plt.plot(x, y3, color='orange', label='λ = 2.0')
    plt.legend()
    plt.show()


def visualize_snd():
    x = np.arange(-4, 4, 0.25)
    y = scipy.stats.norm.cdf(x)
    plt.plot(x, y)
    plt.show()


def main():
    visualize_snd()


if __name__ == '__main__':
    main()
