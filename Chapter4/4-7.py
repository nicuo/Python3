#!/usr/bin/env python

def main():
    for thing in ('Got %s' % number for number in range(10)):
        print(thing)

if __name__ == '__main__':
    main()
