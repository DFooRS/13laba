#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_elem(*args):
    if args:
        values = tuple(float(arg) for arg in args)

        sum_num = 0
        max_num = 0
        for i, item in enumerate(values):
            if item > max_num:
                n = i
                max_num = item
        for item in values[:n]:
            if item > 0:
                sum_num += item

        return sum_num

    else:
        return None


if __name__ == "__main__":
    print(sum_elem(3, -2, 1, 5, 4, 43, 9, -4, 7))