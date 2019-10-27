import csv

# function that reads the csv file.
# opens the csv file and converts it to the DictReader object and casts that to list. 
# encapsulates all of the dictionaries into a list
def get_csv_data():
    with open("Mobile_Phone_Masts_01.04.2019a.csv") as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        return list(csv_reader)


csv_data = get_csv_data() 
print(csv_data)