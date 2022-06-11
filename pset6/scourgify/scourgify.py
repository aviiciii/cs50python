from sys import argv, exit
import csv

def main():
    readfile, writefile = get_filenames(argv)
    check_csv(readfile)
    check_csv(writefile)

    firstnames=[]
    lastnames=[]
    house=[]
    try:
        with open(readfile,'r') as file:
            reader=csv.DictReader(file)
            for row in reader:
                last, first=row['name'].split(',')
                lastnames.append(last.strip())
                firstnames.append(first.strip())
                house.append(row['house'])
    except FileNotFoundError:
        exit('File does not exist')
    except Exception as arg:
        exit(arg)

    with open(writefile,'w') as file:
        fieldnames=['first','last','house']
        writer=csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(firstnames)):
            writer.writerow({'first': firstnames[i],'last': lastnames[i],'house': house[i],})



def get_filenames(arguments):
    if len(arguments) != 3:
        if len(arguments) < 3:
            exit('Too few command-line arguments')
        else:
            exit('Too mant command-line arguments')
    return [argv[1],argv[2]]

def check_csv(filename):
    dot = filename.find('.')
    if filename[dot:] != '.csv':
        exit('Not a CSV file')

if __name__ == '__main__':
    main()