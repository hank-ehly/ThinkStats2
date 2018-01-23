from __future__ import print_function, division

import matplotlib.pyplot as plt
from collections import Counter

import nsfg
import thinkstats2
import thinkplot
import probability


def new_pmf(data):
    d = data.dropna()
    total = len(d)
    cnt = Counter(d)
    pmf = cnt.copy()
    for x in cnt:
        pmf[x] = cnt[x] / total
    return pmf


def show_birthwgt_lb_hist():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    val_counts = live.birthwgt_lb.value_counts()
    plt.bar(val_counts.index, val_counts.values, label='birthwgt_lb')
    plt.legend()
    plt.show()


def show_birthwgt_lb_pmf():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    pmf = new_pmf(live.birthwgt_lb)
    plt.bar(list(pmf.keys()), list(pmf.values()), label='birthwgt_lb')
    plt.legend()
    plt.show()


def show_prglngth_pmf():
    preg = nsfg.ReadFemPreg()
    live = preg[preg.outcome == 1]
    pmf = new_pmf(live['prglngth'])
    plt.bar(list(pmf.keys()), list(pmf.values()), label='prglngth')
    plt.xlabel('Pregnancy length (weeks)')
    plt.ylabel('Pmf')
    plt.legend()
    plt.show()


def exercise_3_1():
    preg = nsfg.ReadFemPreg()
    resp = nsfg.ReadFemResp()
    pmf = thinkstats2.Pmf(resp.numkdhh)
    thinkplot.Pmf(pmf)
    thinkplot.Config(xlabel='Number of children', ylabel='PMF')

    biased_pmf = probability.BiasPmf(pmf, label='Biased')
    thinkplot.PrePlot(2)
    thinkplot.Pmfs([pmf, biased_pmf])
    thinkplot.Config(xlabel='Number of children', ylabel='PMF')

    print('Mean diff: %s' % (pmf.Mean() - biased_pmf.Mean()))  # Mean diff: -1.3794739456204512

    thinkplot.Show()


def pmf_mean(pmf):
    mean = 0
    for k, v in pmf.Items():
        mean += (k * v)
    return mean


def pmf_var(pmf):
    var = 0
    for k, v in pmf.Items():
        var += v * (k - pmf_mean(pmf)) ** 2
    return var


def exercise_3_2():
    pmf = thinkstats2.Pmf([1, 1, 1, 2, 3, 4, 5])
    assert pmf_mean(pmf) == pmf.Mean()
    assert pmf_var(pmf) == pmf.Var()
    print('All tests pass')


if __name__ == '__main__':
    exercise_3_2()
