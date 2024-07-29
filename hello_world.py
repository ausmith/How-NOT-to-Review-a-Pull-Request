#!/usr/bin/env python

import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    return parser.parse_args()


def is_name_significant(name):
    # Are there repeat characters
    characters = sorted(list(name))
    seen_chars, dup_chars = [], []
    for char in characters:
        if char in seen_chars:
            dup_chars.append(char)
        else:
            seen_chars.append(char)
    # Is it one word
    num_words = len(name.split())
    # Is it a palindrome
    palindrome = (name == name[::-1])
    print("How special is the name you entered?")
    print("  Name entered: '{}'".format(name))
    print("  Has duplicate characters: {}".format(len(dup_chars) > 0))
    print("  Is palindrome: {}".format(palindrome))


def fancy_print_name(name):
    print("==========================")
    print("Hello {}!".format(args.name))
    print("==========================")


if __name__ == "__main__":
    args = parse_args()
    # Calculate the name
    if not args.name or len(args.name) < 1:
        print("Please enter a name for me to say hello.")
    else:
        fancy_print_name(args.name)
        is_name_significant(args.name)
