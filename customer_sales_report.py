import csv


def main():
    infile = open('sales.csv', 'r')
    outfile = open('salesreport.csv', 'w')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)

    total = 0
    previous_id = None
    rollup = []
    # for row in csvfile:
    # current_id = row[0]
    # if previous_id == current_id:
    #    total += float(row[3])
    # else:
    #   previous_id = current_id
    #  total = float(row[3])
    for row in csvfile:
        current_id = int(row[0])
        if previous_id != current_id:
            if previous_id is not None:
                rollup.append([previous_id, round(total, 2)])
            previous_id = current_id
            total = (float(row[3]) + float(row[4]) + float(row[5]))
        else:
            total += (float(row[3]) + float(row[4]) + float(row[5]))

    outfile.write('Customer ID ' + ' Total Pay' + '\n')

    for row in rollup:
        outfile.write(str(row[0]) + '          ' + str(row[1]))
        outfile.write('\n')

    outfile.close()


main()
