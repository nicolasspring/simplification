#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Authors: Nicolas Spring

import argparse
import sys

from SARI import SARIdoc


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=str,
        help="source file",
        metavar="SOURCE",
    )
    parser.add_argument(
        "--hypothesis",
        type=str,
        help="hypothesis file",
        metavar="HYPOTHESIS",
    )
    parser.add_argument(
        "--reference",
        type=str,
        help="referece file",
        metavar="REFERENCE",
    )
    args = parser.parse_args()
    return args


def main(args: argparse.Namespace):
    sys.stdout.write(str(SARIdoc(args.source, args.hypothesis, args.reference)))


if __name__ == "__main__":
    args = parse_args()
    main(args)
