from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

import nsfg
import first
import thinkstats2
import thinkplot

preg = nsfg.ReadFemPreg()
live = preg[preg.outcome == 1]


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


if __name__ == '__main__':
    show_prglngth_pmf()
