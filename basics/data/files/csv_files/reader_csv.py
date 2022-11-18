import csv

with open("data.csv") as csv_file:
    csv_reader = csvreader(csv_file, delimiter=",", quotechar='"') # Each roe is a sequence of data that can be acessed using endex number (e;g; row[0]
    for row in csv_reader:
        print(row[0]
