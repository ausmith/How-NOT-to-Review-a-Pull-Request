#!/bin/bash

import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    print("Hlelo {}!".format(args.name))
