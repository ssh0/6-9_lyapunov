#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.
#
# 計算機実習
# 問題6.9 リアプノフ指数
# -a 素朴な方法でロジスティック写像のリアプノフ指数を求める
# 例:
#   r        = 0.91    : control parameter
#   delta_x0 = 0.00005 : width of initial values
#   dx       = 0.001   : step size of x0


import matplotlib.pylab as plt
import SetParameter as sp  # 同じディレクトリにSetParameter.pyを置く
import CalculateLambda as cl  # 同じディレクトリにCalculateLambda.pyを置く


def assignment():
    global r, delta_x0, dx
    r = float(window.entry[0].get())
    delta_x0 = float(window.entry[1].get())
    dx = float(window.entry[2].get())
    window.quit()


def plot_x0_lambda(x0, lyapunovs):
    plt.plot(x0, lyapunovs,
             label='\n' + r'$r=$' + str(r) + '\n'
             + '$\Delta x_{0}\ (:\mathrm{width\ of\ initial\ values})=$'
             + str(delta_x0) + '\n'
             + '$dx\ (:\mathrm{step\ size\ of\ }x_{0})=$'
             + str(dx)
             )


def plot_average_lambda(x0, lyapunovs):
    ave_lambda = sum(lyapunovs) / len(x0)
    plt.plot([0, 1], [ave_lambda] * 2,
             label=r'$\mathrm{average\ of\ } \lambda=$' + str(ave_lambda)
             )
    plt.gca().set_xlim(0, 1)
    plt.gca().set_ylim(min(lyapunovs) - 0.1, max(lyapunovs) + 0.1)
    plt.xlabel(r'$x_{0}$', fontsize=16)
    plt.ylabel(r'$\lambda$', fontsize=16)
    plt.title('Lyapunov index')
    plt.legend(loc="best")

if __name__ == '__main__':

    window = sp.SetParameter()
    parameters = [{'r': 0.91}, {'delta_x0': 0.000001}, {'dx': 0.01}]
    window.show_setting_window(parameters, {'OK': assignment})

    calculate = cl.CalculateLambda()
    calculate.set_parameter(r, delta_x0, dx)
    calculate.prepare_x0_and_lambda()

    plot_x0_lambda(calculate.x0, calculate.lyapunovs)
    plot_average_lambda(calculate.x0, calculate.lyapunovs)

    plt.show()
