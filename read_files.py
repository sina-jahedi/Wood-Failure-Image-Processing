import csv
from os import listdir

# read the files in /image folder and import the wood failure percent one by one into a .csv file
#create a new .csv file
filename = "summary.csv"
with open(filename, 'w', newline="") as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # field names
    fields = ['ID', 'wood failure left', 'wood failure right']
    # writing the fields
    csvwriter.writerow(fields)

    all_files = [file for file in listdir('results/') if file[-4:] == '.txt']
    for file in all_files:
        if file[-5] == 'L':
            current_file = open("results/{}".format(file), "r")
            Lines = current_file.readlines()
            ID = Lines[0]
            wood_failure_left = float(Lines[7].lstrip('%wood=t/'))

        else:
            current_file = open("results/{}".format(file), "r")
            Lines = current_file.readlines()
            ID = Lines[0]
            wood_failure_right = float(Lines[7].lstrip('%wood=t/'))
            # data rows of csv file
            rows = [[ID[:-2], wood_failure_left, wood_failure_right]]
            # writing the data rows
            csvwriter.writerows(rows)
