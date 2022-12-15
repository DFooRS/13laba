#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def aver_geom(*args):
    if args:
        mult = 1
        n = 0
        for item in args:
            mult *= item
            n += 1
        n = 1 / n

        return math.pow(mult, n)

    else:
        return None


if __name__ == "__main__":
    print(aver_geom(5, 4, 2))
