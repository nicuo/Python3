def main():
    with open('test.txt','rt') as infile:
        test2 = infile.read()
        
    test1 ='This is a test of the emergency text system'
    print(test1 == test2)



if __name__ == '__main__':
    main()
