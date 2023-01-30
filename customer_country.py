import csv

def main():
    infile = open('customers.csv', 'r')
    outfile = open('customers_country.csv', 'w')

    csvfile = csv.reader(infile, delimiter=',')

    index = 0 
    for record in csvfile:
        outfile.write(record[1] + ' ' + record[2] + ',' + ' ' + record[4])
        index += 1
        outfile.write('\n')

    outfile.write('Customers read: ' + str(index))

    outfile.close()


main()
