#!/bin/bash

import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("name")
    return parser.parse_args()


def add_value():
  bsness = 'foo'
  product = 'bar'
  value = "{} makes {}".format(bsness, product)
  return value


if __name__ == "__main__":
    args = parse_args()
    print("Hello {}!".format(args.name))
    print("Provided value in a theoretical world where we have this all figured out and things work just right: {}".format(add_value()))
