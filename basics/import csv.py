import csv

with open("data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter= ',', quotechar='"'
    for row in csv_reader:
        print(row[0])
# Using csv.reader reads by
