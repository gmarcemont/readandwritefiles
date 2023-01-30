import csv


def main():
    infile = open('sales.csv', 'r')
    outfile = open('salesreport.csv', 'w')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    for row in csvfile:
        if 

    outfile.write('Customer ID', 'Total\n')

    outfile.close()


main()
