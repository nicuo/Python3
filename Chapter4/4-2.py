#!/usr/bin/env python

def main():
    gusess_me = 7
    start = 1
    while True:
        if start < gusess_me:
            print("too low")
        elif start == gusess_me:
            print("found it!")
            break
        else:
            # under lines is not used.
            print("oops")
            break
        start += 1



if __name__ == '__main__':
    main()
