def main(): 
    path = input('Enter path to file: ') 
    with open(path, 'rt') as fs: 
        lines = fs.readlines() 
        print('{0:^6}{1:^12}{2:^12}'.format('Line', 'Char count', 'Word count')) 
        n = 1 
        for line in lines: 
            line = line.rstrip('\n') 
            print('{0:^6}{1:^12}{2:^12}'.format(n, len(line), len(line.split()))) 
            n += 1 
 
 
if __name__ == '__main__': 
    main()
