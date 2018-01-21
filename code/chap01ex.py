"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2
import thinkplot


def main(script):
    """Tests the functions in this module.

    script: string script name
    """

    dct = thinkstats2.ReadStataDct('2002FemResp.dct')
    df = dct.ReadFixedWidth('2002FemResp.dat.gz', compression='gzip')
    nsfg.CleanFemResp(df)

    dct2 = thinkstats2.ReadStataDct('2002FemPreg.dct')
    df2 = dct2.ReadFixedWidth('2002FemPreg.dat.gz', compression='gzip')
    nsfg.CleanFemPreg(df2)

    hist1 = thinkstats2.Hist(df['pregnum'].values)
    hist2 = thinkstats2.Hist(df2['pregnum'].values)

    thinkplot.subplot(1, 1, 2)
    thinkplot.Hist(hist1)

    thinkplot.subplot(2, 1, 2)
    thinkplot.Hist(hist2)

    thinkplot.show()

    # print(df['pregnum'].value_counts().sort_index(), df2['pregnum'].value_counts().sort_index())

    print('%s: All tests passed.' % script)


if __name__ == '__main__':
    main(*sys.argv)
