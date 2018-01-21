from __future__ import print_function, division

import matplotlib.pyplot as plt
from collections import Counter

import nsfg
import thinkstats2
import thinkplot
import probability

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]
resp = nsfg.ReadFemResp()


def new_pmf(data):
    d = data.dropna()
    total = len(d)
    cnt = Counter(d)
    pmf = cnt.copy()
    for x in cnt:
        pmf[x] = cnt[x] / total
    return pmf


def show_birthwgt_lb_hist():
    val_counts = live.birthwgt_lb.value_counts()
    plt.bar(val_counts.index, val_counts.values, label='birthwgt_lb')
    plt.legend()
    plt.show()


def show_birthwgt_lb_pmf():
    pmf = new_pmf(live.birthwgt_lb)
    plt.bar(list(pmf.keys()), list(pmf.values()), label='birthwgt_lb')
    plt.legend()
    plt.show()


def show_prglngth_pmf():
    pmf = new_pmf(live['prglngth'])
    plt.bar(list(pmf.keys()), list(pmf.values()), label='prglngth')
    plt.xlabel('Pregnancy length (weeks)')
    plt.ylabel('Pmf')
    plt.legend()
    plt.show()


def ex_31():
    pmf = thinkstats2.Pmf(resp.numkdhh)
    thinkplot.Pmf(pmf)
    thinkplot.Config(xlabel='Number of children', ylabel='PMF')

    biased_pmf = probability.BiasPmf(pmf, label='Biased')
    thinkplot.PrePlot(2)
    thinkplot.Pmfs([pmf, biased_pmf])
    thinkplot.Config(xlabel='Number of children', ylabel='PMF')

    print('Mean diff: %s' % (pmf.Mean() - biased_pmf.Mean()))  # Mean diff: -1.3794739456204512

    thinkplot.Show()


if __name__ == '__main__':
    ex_31()
