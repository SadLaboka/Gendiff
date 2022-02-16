#!/usr/bin/env python3
import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='FIRST_FILE')
    parser.add_argument('second_file', metavar='SECOND_FILE')
    parser.add_argument('-f', '--format', help='set format of output', required=False)
    args = parser.parse_args()

    print(args.accumulate(args))


if __name__ == '__main__':
    main()
