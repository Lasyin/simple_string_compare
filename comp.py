#!/usr/bin/env python

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('str1', action='store')
    parser.add_argument('str2', action='store')
    parser.add_argument('-cut', help="Exclude this segment from the comparison.", action="store")

    args = parser.parse_args()
    str1 = str(args.str1)
    str2 = str(args.str2)
    if(args.cut):
        print("Cut out: " + args.cut)
        str1 = str1.replace(str(args.cut), '')
        str2 = str2.replace(str(args.cut), '')

    print("Comparing...\n" + str1 + "\nTo\n" + str2 +"\n...\n")

    if(str1 == str2):
        print("Equal")
    elif(str1.lower() == str2.lower()):
        print("Equal if case insensitive")
    else:
        print("Not Equal")
