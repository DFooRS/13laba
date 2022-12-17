#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def aver_even(*args):
    if args:
        sum_e = 0
        n = 0
        for arg in args:
            if arg % 2 == 0:
                sum_e += arg
                n += 1
        return sum_e / n

    else:
        return None


if __name__ == "__main__":
    print(aver_even(5, 4, 2, 7, 3, 12))