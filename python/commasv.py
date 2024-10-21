import csv

# with open("/workspaces/My-Old-Codes/python/EXCEL DATA.csv", "r") as file:
#     reader = csv.reader(file)
#     for row in sorted(reader, reverse=True):
#         print(row[0])  # Process each row as needed
        
with open("/workspaces/My-Old-Codes/python/EXCEL DATA.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in sorted(reader):
        print(row["No"])  # Process each row as needed