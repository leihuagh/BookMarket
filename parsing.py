import csv

delim = input("Используемый разделитель: ")
result = {}

with open('list.csv', 'r') as my_file:
    for line in csv.reader(my_file):
        s = line[0].split(delim)
        result.update({s[0]: [s[1], s[2]]})

print(result)
