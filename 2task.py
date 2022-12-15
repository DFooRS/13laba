#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def aver_garm(*args):
    if args:
        n = 0
        sum = 0
        for item in args:
            sum += 1 / item
            n += 1

        return n / sum

    else:
        return None


if __name__ == "__main__":
    print(aver_garm(5, 4, 2))