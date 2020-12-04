#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Authors: Nicolas Spring

import argparse
import sys

from SARI import SARIsent


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=str,
        help="source segment",
        metavar="SOURCE",
    )
    parser.add_argument(
        "--hypothesis",
        type=str,
        help="hypothesis segment",
        metavar="HYPOTHESIS",
    )
    parser.add_argument(
        "--references",
        type=str,
        nargs="+",
        help="referece segments",
        metavar="REFERENCES",
    )
    args = parser.parse_args()
    return args


def main(args: argparse.Namespace):
    sys.stdout.write(str(SARIsent(args.source, args.hypothesis, args.references)))


if __name__ == "__main__":
    args = parse_args()
    main(args)
