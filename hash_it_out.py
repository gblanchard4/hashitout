#!/usr/bin/env python
import argparse
import glob
import hashlib
from collections import defaultdict

__author__ = "Gene Blanchard"
__email__ = "me@geneblanchard.com"

'''
Hash all the files in a directory
and remove deplicates
'''

def md5_hash(file):
    return hashlib.md5(open(file).read()).hexdigest()

def main():
    # Argument Parser
    parser = argparse.ArgumentParser(description='<This is what the script does>')

    # Input directory
    parser.add_argument('-i', '--input', dest='input', help='The input file')
    # Debug mode
    parser.add_argument('-r', '--remove', dest='remove', action="store_true", help='Remove duplicate files')

    # Parse arguments
    args = parser.parse_args()
    indir = args.input
    remove = args.remove

    # Build a hashmap
    globber = "{}/*".format(indir)
    files = glob.glob(globber)
    hash_dict = {md5_hash(file): file for file in files}
    hash_dict = defaultdict(list)
    for file in files:
        hash_dict[md5_hash(file)].append(file)

if __name__ == '__main__':
    main()
