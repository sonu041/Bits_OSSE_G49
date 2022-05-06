#!/usr/bin/env python3

from argparse import ArgumentParser

if __name__ == "__main__":

    ap = ArgumentParser(
        description="CLI password generator"
    )
    ap.add_argument(
        "-l", "--len", help="Password length",
        type=int, default=15, metavar="INT"
    )

    args = ap.parse_args()
    print(args)
