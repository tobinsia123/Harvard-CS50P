from tabulate import tabulate
import sys

def main():
    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
        if len(sys.argv) == 2:
            print(csvCheck(lines))
        elif len(sys.argv) > 2:
            raise IndexError
    except FileNotFoundError:
        sys.exit('File does not exist')
    except IndexError:
        if len(sys.argv) > 2:
            sys.exit('Too many command-line arguments')
        elif len(sys.argv) < 2:
            sys.exit('Too few command-line arguments')


def tabulateFile(lines):
    x = []
    for line in lines:
        item = line.rstrip().split(',')
        x.append(item)
    return tabulate(x, headers='firstrow', tablefmt='grid')


def csvCheck(lines):
    prefix, suffix = sys.argv[1].split('.')
    if suffix == 'csv':
        return tabulateFile(lines)
    else:
        sys.exit('Not a CSV file')


if __name__ == '__main__':
    main()

