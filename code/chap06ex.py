import brfss
import thinkstats2
import thinkplot
import hinc
import hinc2
import numpy as np


def show_adult_weight_pdf():
    df = brfss.ReadBrfss(nrows=None)
    adult_weights = df.wtkg2.dropna()
    pdf = thinkstats2.EstimatedPdf(adult_weights)
    thinkplot.Pdf(pdf, label='Adult weight')
    thinkplot.Config(xlabel='Adult weight (kg)', ylabel='PDF')
    thinkplot.Show()


def exercise_6_1():
    income_df = hinc.ReadData()
    log_sample = hinc2.InterpolateSample(income_df, 6.0)

    # log10 CDF
    log_cdf = thinkstats2.Cdf(log_sample)
    # thinkplot.Cdf(log_cdf)
    # thinkplot.Config(xlabel='Household income (log $)', ylabel='CDF')

    # $ based CDF
    sample = np.power(10, log_sample)
    cdf = thinkstats2.Cdf(sample)
    # thinkplot.Cdf(cdf)
    # thinkplot.Config(xlabel='Household income ($)', ylabel='CDF')

    mean = thinkstats2.Mean(sample)
    median = thinkstats2.Median(sample)
    skewness = thinkstats2.Skewness(sample)
    pearson_skewness = thinkstats2.PearsonMedianSkewness(sample)
    print('Mean: %s, Median: %s, Skewness: %s, Pearson\'s Skewness: %s' % (mean, median, skewness, pearson_skewness))
    print('What fraction of households report a taxable income below the mean? %s' % cdf.PercentileRank(mean))

    """ 
    Q: How do the results depend on the assumed upper bound?
    
    If the upper bound increases, a greater number of households appear to report a taxable income below the mean.
    When the upper bound is 6.0 ($1,000,000) , the fraction is roughly 66%
    When the upper bound is 7.0 ($10,000,000), the fraction is roughly 86%
    
    Q: What happens to the skew if the upper bound is 10 million?
    
    When the upper bound is $1,000,000 , the skew is 4.95, and pearson's skew is 0.74
    When the upper bound is $10,000,000, the skew is 11.6, and pearson's skew is 0.39
    """


def main():
    exercise_6_1()


if __name__ == '__main__':
    main()
