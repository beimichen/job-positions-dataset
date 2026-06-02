import csv

with open('positions_lookup.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if not row:
            print("This is empty")
