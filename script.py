import csv

# function that reads the csv file.
# opens the csv file and converts it to the DictReader object and casts that to list. 
# encapsulates all of the dictionaries into a list.
def get_csv_data():
    with open("Mobile_Phone_Masts_01.04.2019a.csv") as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        return list(csv_reader)


# function that sorts through the data, sorted by the key using lambda in ascending order returning the first 5.
def rent_costs_in_acsending_order(data):
    result = sorted(data, key=lambda d: float(d['Current Rent']))
    return result[:5]



csv_data = get_csv_data()
sorted_by_ascending = rent_costs_in_acsending_order(csv_data)
print(sorted_by_ascending)

