import matplotlib.pyplot as plt
import numpy as np


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


def main():
    exponential_distribution_plot()


if __name__ == '__main__':
    main()
