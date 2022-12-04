#!/usr/bin/python3
import sys



argv = sys.argv[1:]



print("Number of argument(s):", len(argv))



if len(argv) == 1:

    print("Argument:", end="")

else:

    print("Arguments:", end="")

    

if len(argv) == 0:

    print(".")

else:

    print(":")

    

for index, arg in enumerate(argv):

    print(index+1, ":", arg)
