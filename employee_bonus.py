import csv


def main():
    infile = open('EmployeePay.csv', 'r')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    for record in csvfile:
        print('ID: ' + record[0])
        print('First Name: ' + record[1])
        print('Last Name: ' + record[2])
        print('Employee Salary: ' + record[3])
        print('Bonus: ' + record[4])
        input()


main()
