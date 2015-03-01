#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.
#
# 計算機実習
# 問題6.9 リアプノフ指数
# -b 教科書で示されたアルゴリズムを用いて
# ロジスティック写像のリアプノフ指数を求める。
#

import matplotlib.pylab as plt
import array as array
import numpy as np
import multiprocessing as mp

# --- set parameters ---

r0 = 0.76
rmax = 1.0
dr = 0.001
ntransient = 1000
n_calc = 100000
x0 = 0.5

nmax = ntransient + n_calc

pr = mp.cpu_count() * 2

def lambda_for_r():
    if (rmax - r0) % dr == 0:
        count = int((rmax - r0) / dr) - 1
    else:
        count = int((rmax - r0) / dr)
    r = [r0 + dr*n for n in np.arange(count + 1)]
    r.append(rmax)
    r = np.array(r)
    _lambda = array.array('f')
    pool = mp.Pool(pr)

    _lambda = np.array(pool.map(get_lambda_r, r))
    return r, _lambda


def get_lambda_r(r):
    def function(x_i, r):
        return 4.0 * r * x_i * (1.0 - x_i)

    x = array.array('d')
    x.append(x0)
    for i in np.arange(nmax):
        x.append(function(x[i], r))

    def operate(cx):
        return np.log(abs(4.0 * r * (1.0 - 2.0 * cx)))

    cutted_x = x[ntransient:nmax]
    edited_x = map(operate, cutted_x)
    lambda_r = sum(edited_x) / len(edited_x)
    return lambda_r

r_and_lambda = lambda_for_r()
plt.gca().set_xlim(r0, rmax)
plt.gca().set_ylim(-2.0, 1.0)
plt.scatter(r_and_lambda[0], r_and_lambda[1], color='b', s=0.5, marker='.')
plt.plot([r0, rmax], [0, 0], 'r--')
plt.xlabel(r'$r$', fontsize=16)
plt.ylabel(r'$\lambda$', fontsize=16)
plt.title('Lyapunov index')
plt.show()
