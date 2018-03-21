import first
import thinkstats2
import thinkplot
import matplotlib.pyplot as plt
import numpy as np


def show_birth_weight_vs_mother_age():
    """
    Using data from the NSFG, make a scatter plot of birth weight versus mother's age
    """
    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

    plt.scatter(live.totalwgt_lb, live.agepreg, alpha=0.05)
    plt.xlabel('Birth weight (lb)')
    plt.ylabel("Mother's age")
    plt.show()


def plot_percentiles_of_birth_weight_vs_mother_age():
    """
    Plot percentiles of birth weight versus mother's age.
    """
    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])

    # bin one variable and plot percentile of the other
    bins = np.arange(10, 44)
    indices = np.digitize(live.agepreg, bins)
    groups = live.groupby(indices)

    # compute the mean mother age and the CDF of total weight
    ages = [group.agepreg.mean() for i, group in groups]
    cdfs = [thinkstats2.Cdf(group.totalwgt_lb) for i, group in groups]

    # plot percentiles of mother's age versus total weight
    for percent in [75, 50, 25]:
        weights = [cdf.Percentile(percent) for cdf in cdfs]
        label = '%dth' % percent
        thinkplot.Plot(ages, weights, label=label)

    thinkplot.Config(xlabel="Mother's age", ylabel="Total weight (lb)")
    thinkplot.Show()


def compute_correlations():
    """
    Compute Pearson's and Spearman's correlations
    """
    live, firsts, others = first.MakeFrames()
    live = live.dropna(subset=['agepreg', 'totalwgt_lb'])
    pearson_corr = thinkstats2.Corr(live.totalwgt_lb, live.agepreg)
    spearman_corr = thinkstats2.SpearmanCorr(live.totalwgt_lb, live.agepreg)
    print("Pearson's correlation: %s, Spearman's correlation: %s" % (pearson_corr, spearman_corr))


def exercise_7_1():
    """
    Q: How would you characterize the relationship between these variables?
    
    1) The scatter plot doesn't show a strong relationship between the two variables
    2) Plotting percentiles of weight against mother height shows a non-linear relationship
    3) Pearson's and Spearman's correlations are both near 0, which signifies a weak relationship
    """

    # show_birth_weight_vs_mother_age()
    # plot_percentiles_of_birth_weight_vs_mother_age()
    compute_correlations()


def main():
    exercise_7_1()


if __name__ == '__main__':
    main()
