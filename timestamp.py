#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2014 Fredy Wijaya
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#  
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import argparse
import datetime


def create_args():
    arg_parser = argparse.ArgumentParser(description='A script to convert date to time in millis and vice-versa',
                                         formatter_class=lambda prog: argparse.HelpFormatter(prog,
                                                                                             max_help_position=100))
    arg_parser.add_argument('-n', '--now', dest='now', action='store_true',
                            help='print the current date in time in millis')
    arg_parser.add_argument('-f', '--from', dest='frm', type=str,
                            help='print time in millis to date (mm-dd-yyyy)')
    arg_parser.add_argument('-t', '--to', dest='to', type=str,
                            help='print date (mm-dd-yyyy) to millis')

    if len(sys.argv) == 1:
        arg_parser.print_help()
        sys.exit(0)

    return arg_parser.parse_args()


def show(args):
    if args.now:
        print int(datetime.datetime.now().strftime('%s')) * 1000
    elif args.frm is not None:
        frm_split = args.frm.split('-')
        month = int(frm_split[0])
        day = int(frm_split[1])
        year = int(frm_split[2])
        print int(datetime.datetime(year, month, day).strftime('%s')) * 1000
    elif args.to is not None:
        print datetime.datetime.fromtimestamp(int(args.to) / 1000).strftime('%m-%d-%Y')


if __name__ == '__main__':
    args = create_args()
    show(args)