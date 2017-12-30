#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 stcarolas <stcarolas@homeGround>
#
# Distributed under terms of the MIT license.
import fileinput
import subprocess

if __name__ == '__main__':
    with open("/tmp/m1","w") as fp:
        for line in fileinput.input():
            fp.write(line)
    result = []
    with open("/tmp/m1","r") as fp:
        while True:
            data = fp.readline()
            if len(data) == 0:
                break
            result.append(data)
    print(result[0])
