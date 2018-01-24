from __future__ import print_function, division

import matplotlib.pyplot as plt
from collections import Counter

import nsfg
import thinkstats2
import thinkplot
import probability
import first
import pandas as pd
import numpy as np


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


def exercise_3_3():
    live, firsts, others = first.MakeFrames()
    preg_map = nsfg.MakePregMap(live)

    # (1) First try (comparing first prglngth with mean of 2nd+)
    # multi_birth_case_idx = {caseid: prg_idx for caseid, prg_idx in preg_map.items() if len(prg_idx) > 1}.keys()
    # diffs = []
    # for idx, caseid in enumerate(multi_birth_case_idx):
    #     first_prglngth = firsts[firsts.caseid == caseid].prglngth.values[0]
    #     other_prglngth_mean = others[others.caseid == caseid].prglngth.values.mean()
    #     diffs.append(np.diff([first_prglngth, other_prglngth_mean]))
    #
    # df = pd.DataFrame(diffs)
    # mean_diff = df.mean()
    # print(mean_diff)  # -0.11808

    # (2) Book solution (only compares first and second prglngth)
    hist = thinkstats2.Hist()
    for caseid, prg_idx in preg_map.items():
        if len(prg_idx) >= 2:
            pair = live.loc[prg_idx[0:2]].prglngth
            diff = np.diff(pair)[0]
            hist[diff] += 1

    thinkplot.Hist(hist)
    thinkplot.Show()
    pmf = thinkstats2.Pmf(hist)
    print(pmf.Mean())  # -0.0563674321503

    # (3) Use book solution code to compare first and 2nd+ prglngth
    # Implementation comparing first pregnancy length with mean of 2nd+ (rather than just 2nd)
    # hist = thinkstats2.Hist()
    # for caseid, prg_idx in preg_map.items():
    #     if len(prg_idx) >= 2:
    #         pair = [live.loc[prg_idx[0]].prglngth, live.loc[prg_idx[1]].prglngth]
    #         diff = np.diff(pair)[0]
    #         hist[diff] += 1
    #
    # # thinkplot.Hist(hist)
    # # thinkplot.Show()
    # pmf = thinkstats2.Pmf(hist)
    # print(pmf.Mean())  # -0.118079718549


def exercise_3_4():
    pass


if __name__ == '__main__':
    exercise_3_3()
