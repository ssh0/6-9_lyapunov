#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.
#
# 計算機実習
# 問題6.9 リアプノフ指数
# -a0
# \ln | \Delta x_{n} / \Delta x_{0} |のグラフの描画

import matplotlib.pylab as plt
import array as array
import numpy as np
import SetParameter as sp  # 同じディレクトリにSetParameter.pyを置く


def assignment():
    global r, x0, delta_x0, nmax
    r = float(window.entry[0].get())
    x0 = float(window.entry[1].get())
    delta_x0 = float(window.entry[2].get())
    nmax = int(window.entry[3].get())
    window.quit()
    mapping(r, x0, delta_x0, nmax)


def func(x_i, r):
    return 4.0 * r * x_i * (1 - x_i)


def mapping(r, x0, delta_x0, nmax):  # グラフの描画
    x1 = array.array('d')
    x1.append(x0)
    x2 = array.array('d')
    x2.append(x0 + delta_x0)
    lya = array.array('d')
    for count in range(nmax):
        x1.append(func(x1[-1], r))
        x2.append(func(x2[-1], r))
        l = np.log(abs((x2[-1] - x1[-1]) / delta_x0))
        lya.append(l)
    n = range(1, nmax + 1)
    plt.plot(n, lya,
             label=r'$r=$' + str(r) + ' : '
             + r'$x_{0}=$' + str(x0) + ' : '
             + r'$\Delta x_{0}=$' + str(delta_x0)
             )
    plt.gca().set_xlim(0, nmax)
    plt.gca().set_ylim(min(lya) - 0.3, max(lya) + 0.3)
    plt.xlabel(r'$n$', fontsize=16)
    plt.ylabel(r'$\ln | \Delta x_{n} / \Delta x_{0}| $', fontsize=16)
    plt.title('Graph of 'r'$\ln | \Delta x_{n} / \Delta x_{0} |$')
    plt.legend(loc="best")
    plt.show()

if __name__ == '__main__':
    parameters = [{'r': 0.91}, {'x0': 0.5},
                  {'delta_x0': 0.000001}, {'nmax': 200}]
    window = sp.SetParameter()
    window.show_setting_window(parameters, {'OK': assignment})
