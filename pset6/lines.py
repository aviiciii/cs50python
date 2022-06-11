from sys import argv, exit

if len(argv) != 2:
    if len(argv) < 2:
        exit('Too few command-line arguments')
    else:
        exit('Too mant command-line arguments')

filename = argv[1]

dot = filename.find('.')
if filename[dot:] != '.py':
    exit('Not a Python file')

lines = 0

try:
    with open(filename,'r') as file:
        for line in file:
            if line.isspace():
                continue
            if line.strip().startswith('#'):
                continue
            lines +=1
except FileNotFoundError:
    exit('File does not exist')

print(lines)