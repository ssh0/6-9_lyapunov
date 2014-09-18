#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# written by Shotaro Fujimoto, May 2014.
#

import array as array
import numpy as np
import scipy.optimize as optimize


class CalculateLambda():

    def set_parameter(self, r, delta_x0, dx):
        self.r = r
        self.delta_x0 = delta_x0
        dx = dx

        self.n = int((1.0 - self.delta_x0) / dx)
        self.x0 = np.array([(n + 1) * dx for n in range(self.n)])
        self.x0_plus_delta_x0 = self.x0 + self.delta_x0
        return None

    def prepare_x0_and_lambda(self):

        self.lyapunovs = np.array([self.lambda_for_x0(x1, x2) for x1, x2
                                   in zip(self.x0, self.x0_plus_delta_x0)
                                   ])

    def lambda_for_x0(self, x1, x2):
        r = self.r               # - localize
        delta_x0 = self.delta_x0  # -
        nplot = 50  # Note: This value is determined by some trials.
                    #       It affecs directory the value of lyapunov index.

        def func(x_i):
            return 4.0 * r * x_i * (1.0 - x_i)

        ary1 = array.array('d')
        ary1.append(x1)
        ary2 = array.array('d')
        ary2.append(x2)
        lya = array.array('d')
        lya.append(np.log(abs((ary2[-1] - ary1[-1]) / delta_x0)))
        for count in range(nplot - 1):
            ary1.append(func(ary1[-1]))
            ary2.append(func(ary2[-1]))
            l = np.log(abs((ary2[-1] - ary1[-1]) / delta_x0))
            lya.append(l)

        # -- optimize --

        def fit_func(parameter0, n, lya):
            a = parameter0[0]
            b = parameter0[1]
            residual = lya - (a * n + b)
            return residual

        parameter0 = [1.0, 1.0]
            # initial value of parameters a, b (ln||=a*n+b)
        n = range(1, nplot + 1)
        result = optimize.leastsq(fit_func, parameter0,
                                  args=(np.array(n), np.array(lya))
                                  )
        return result[0][0]
