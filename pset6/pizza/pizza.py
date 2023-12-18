from sys import argv, exit
from tabulate import tabulate
import csv

def main():
    filename = get_filename(argv)
    check_csv(filename)

    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            table = []
            headers = list(next(reader))
            for row in reader:
                table.append([row[0], row[1], row[2]])

        # Move print statement outside the loop
        print(tabulate(table, headers, tablefmt="grid"))

    except FileNotFoundError:
        exit('File does not exist')
    except Exception as arg:
        exit(arg)

def get_filename(arguments):
    if len(arguments) != 2:
        if len(arguments) < 2:
            exit('Too few command-line arguments')
        else:
            exit('Too many command-line arguments')
    return arguments[1]

def check_csv(filename):
    dot = filename.find('.')
    if filename[dot:] != '.csv':
        exit('Not a CSV file')

if __name__ == '__main__':
    main()
