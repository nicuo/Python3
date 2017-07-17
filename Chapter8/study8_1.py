
def main():
    test1 ='This is a test of the emergency text system'
    outfile = open('test.txt','wt')
    outfile.write(test1)
    outfile.close()


if __name__ == '__main__':
    main()
