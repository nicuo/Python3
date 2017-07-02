#!/usr/bin/env python

def main():
    odd = {value for value in range(10) if value % 2 == 1}
    print(odd)


if __name__ == '__main__':
    main()
