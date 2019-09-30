import argparse


parser = argparse.ArgumentParser()
parser.add_argument("word", help="Print the word in upper case letters")

# If option -c is provided than it will have value true based on action attribute.
#  That value will be accessible via attribute value of dest.

parser.add_argument("-c", "--count", action="store_true", dest="count", default=False,
                    help="Count number of character in word")

args = parser.parse_args()
# This way argument can be manipulated.
print(args.word.upper())
args = parser.parse_args()
if args.count:
    print (len(args.word))
