import argparse

parser = argparse.ArgumentParser(description="meow is a cat")
parser.add_argument("-n", type=int, help="number of times")
args = parser.parse_args()

if args.n is not None:
    for _ in range(args.n):
        print("meow")
else:
    print("Please provide the number of times to print 'meow' using the -n option.")
