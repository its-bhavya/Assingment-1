'''program that reads data from a CSV file and prints it to the
console.'''
import csv
file_content = []
with open("C:\\Users\\Lenovo\\Assingment-1-1\\username.csv", "+r") as file:
    reader = csv.reader(file, delimiter=',')
    for i in reader:
        for j in i:
            print(j, end = '\t')
        print()
    
