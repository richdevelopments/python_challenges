import csv

# function that reads the csv file.
# opens the csv file and converts it to the DictReader object and casts that to list. 
# encapsulates all of the dictionaries into a list.
def get_csv_data():
    with open("Mobile_Phone_Masts_01.04.2019a.csv") as csv_file: 
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        return list(csv_reader)


# function that sorts through the data, sorted by the key using lambda, in ascending order returning the first 5.
def rent_costs_in_acsending_order(data):
    result = sorted(data, key=lambda d: float(d['Current Rent']))
    return result[:5]


# list comprehension - creating a new list from items, adding the item for every item in data  
# if the number of Lease Years is equal to 25 append item to list. 
# iterates and checks in one single expression
def lease_of_twenty_five_years(data):
    return [item for item in data if item.get('Lease Years') == '25']


# iterates over items and where tenant name create that as a key and count on how many masts
# added the tenant name to the list and cast the list to a set which will remove any duplicates.
def get_tenant_name_list(data):
    return set([item['Tenant Name'] for item in data])


csv_data = get_csv_data()
sorted_by_ascending = rent_costs_in_acsending_order(csv_data)
lease_years_of_twenty_five = lease_of_twenty_five_years(csv_data)
tenant_names = get_tenant_name_list(csv_data)
print(tenant_names)

