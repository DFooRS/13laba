#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def aver_harm(*args):
    if args:
        n = len(args)
        summa = 0
        for item in args:
            summa += 1 / item

        return n / summa

    else:
        return None


if __name__ == "__main__":
    print(aver_harm(5, 4, 2, 7, 3))
