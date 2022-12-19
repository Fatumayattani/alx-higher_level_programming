#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    count = 0  # keep track of the number of integers printed

    try:

        for i in range(x):

            if isinstance(my_list[i], int):  # check if the element is an integer

                print("{:d}".format(my_list[i]), end=' ')  # print the integer

                count += 1

        print()  # print a new line after printing the integers

    except IndexError:  # handle the case where x is larger than the length of my_list

        pass  # do nothing, just skip the loop

    return count  # return the number of integers printed
