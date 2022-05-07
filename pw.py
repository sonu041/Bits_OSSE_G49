#!/usr/bin/env python3

from argparse import ArgumentParser
from src.pwgen import PwGenerator

if __name__ == "__main__":

    ap = ArgumentParser(
        description="CLI password generator"
    )
    ap.add_argument(
        "-l", "--len", help="Password length",
        type=int, default=15, metavar="INT"
    )

    args = ap.parse_args()
    pw_gen = PwGenerator()      # initialise the class
    pw = pw_gen.generate(       # generate a password
        length=args.len
        length=args.len,
        include_numbers=args.num
    )

    print(pw)                   # print the password
