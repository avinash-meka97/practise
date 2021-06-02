import csv
import traceback

file = open("data.csv", "r")
try:
    csvr = csv.reader(file)
    l = 0
    s = 0
    c = 0
    highest = 0
    highval = 0
    name = ''
    for row in csvr:

        if l > 0 and int(row[2]) > highval:
            highest = l
            highval = int(row[2])
            name = row[0] + " " + row[1]

        l = l + 1



    print(name, " has the highest salary ($", round(highval, 2), ").")

    if l > 0 and row[3] == "Employee":
        s = s + int(row[2])
        c = c + 1
        l = l + 1

    print("The average salary is ", round(s / c, 2), " Dollars.")


except:
    print("File not found")
    traceback.print_exc()
finally:
    file.close();

