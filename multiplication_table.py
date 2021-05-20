#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program shows multiplication table
#    with number inputted from the user


def main():
    # This function shows which is bigger or smaller

    # input
    print("This is a multiplication table from 0 - 10")
    num_string = input("Enter positive integer: ")
    print("")

    # process/# output
    try:
        num = int(num_string)
        for i in range(0, 11):
            if num > 0:
                print(num, 'x', i, '=', num * i)
            else:
                print("Invaid, negative number")
    except Exception:
        print("{} is not an number".format(num_string))
    print("\nDone.")


if __name__ == "__main__":
    main()
