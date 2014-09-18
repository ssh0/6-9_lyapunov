#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.
#
# 計算機実習
# 問題6.9 リアプノフ指数
# 素朴な方法とアルゴリズムで求めたリアプノフ指数の比較
#

import SetParameter as sp  # 同じディレクトリにSetParameter.pyを置く
import CalculateLambda as cl  # 同じディレクトリにCalculateLambda.pyを置く
import array as array
import numpy as np

ntransient = 1000
n_calc = 100000
nmax = ntransient + n_calc


def assignment():
    global r, x0, delta_x0
    r = float(window.entry[0].get())
    x0 = float(window.entry[1].get())
    delta_x0 = float(window.entry[2].get())
    window.quit()


def func(x_i, r):
    return 4.0 * r * x_i * (1.0 - x_i)


def get_lambda_r(function, r):
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

if __name__ == '__main__':

    window = sp.SetParameter()
    parameters = [{'r': 0.91}, {'x0': 0.5}, {'delta_x0': 0.000001}]
    window.show_setting_window(parameters, {'OK': assignment})

    # --- Simple way ---
    calculate = cl.CalculateLambda()
    calculate.r = r
    calculate.delta_x0 = delta_x0
    lya_r = calculate.lambda_for_x0(x0, x0 + delta_x0)

    # --- By algorithm ---
    lambda_r = get_lambda_r(func, r)

    # --- Print the results ---
    print
    print '====== Simple way ====== \n' \
        + 'r = ' + str(r) + ' : x0 = ' + str(x0) \
        + ' : delta_x0 = ' + str(delta_x0) + '\n' \
        + 'lambda = ' + str(lya_r) + '\n'

    print '====== By algorithm ====== \n' \
        + 'r = ' + str(r) + ' : x0 = ' + str(x0) \
        + ' : delta_x0 = ' + str(delta_x0) + '\n' \
        + 'lambda = ' + str(lambda_r) + '\n'
