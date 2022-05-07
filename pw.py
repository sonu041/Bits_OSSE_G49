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

    # pass the CLI argument length to the generator to
    # generate a password of supplied length
    # ./pw.py -l 50 --> returns a pw 50 characters long
    
    pw = pw_gen.generate(       # generate a password
        length=args.len,
        include_numbers=args.num
    )

    print(pw)                   # print the password
