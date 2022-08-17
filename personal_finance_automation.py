import csv

with open("/Users/mara/OneDrive/Github/python/personal_finance_import/SampleCSVFile_11kb.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row[1])
