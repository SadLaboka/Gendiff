#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def main():
    """Print difference between 2 files"""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file', type=str)
    parser.add_argument('second_file', metavar='second_file', type=str)
    parser.add_argument('-f', '--format',
                        help='set format of output',
                        default="stylish",
                        required=False
                        )
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
