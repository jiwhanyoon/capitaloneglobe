import numpy as np
import json

json_data = open("data.json").read()

datas = json.loads(json_data)

first_year = []
second_year = []
third_year = []
fourth_year = []
fifth_year = []
sixth_year = []
seventh_year = []
eighth_year = []
ninth_year = []
tenth_year= []
elev_year = []

for data in datas:
    if data['time'][0:4] == "1964": 
        first_year.append(data['latitude'])
        first_year.append(data['longitude'])
        first_year.append(data['mag'])
    elif data['time'][0:4] == "1965":
        second_year.append(data['latitude'])
        second_year.append(data['longitude'])
        second_year.append(data['mag'])
    elif data['time'][0:4] == "1966":
        third_year.append(data['latitude'])
        third_year.append(data['longitude'])
        third_year.append(data['mag'])
    elif data['time'][0:4] == "1967":
        fourth_year.append(data['latitude'])
        fourth_year.append(data['longitude'])
        fourth_year.append(data['mag'])
    elif data['time'][0:4] == "1968":
        fifth_year.append(data['latitude'])
        fifth_year.append(data['longitude'])
        fifth_year.append(data['mag'])
    elif data['time'][0:4] == "1969":
        sixth_year.append(data['latitude'])
        sixth_year.append(data['longitude'])
        sixth_year.append(data['mag'])
    elif data['time'][0:4] == "1970":
        seventh_year.append(data['latitude'])
        seventh_year.append(data['longitude'])
        seventh_year.append(data['mag'])
    elif data['time'][0:4] == "1971":
        eighth_year.append(data['latitude'])
        eighth_year.append(data['longitude'])
        eighth_year.append(data['mag'])
    elif data['time'][0:4] == "1972":
        ninth_year.append(data['latitude'])
        ninth_year.append(data['longitude'])
        ninth_year.append(data['mag'])
    elif data['time'][0:4] == "1973":
        tenth_year.append(data['latitude'])
        tenth_year.append(data['longitude'])
        tenth_year.append(data['mag'])
    elif data['time'][0:4] == "1974":
        elev_year.append(data['latitude'])
        elev_year.append(data['longitude'])
        elev_year.append(data['mag'])


one = ["1964"]
one.append(first_year)

two = ["1965"]
two.append(second_year)

three = ["1966"]
three.append(third_year)

four = ["1967"]
four.append(fourth_year)

five = ["1968"]
five.append(fifth_year)

six = ["1969"]
six.append(sixth_year)

seven = ["1970"]
seven.append(seventh_year)

eight = ["1971"]
eight.append(eighth_year)

nine = ["1972"]
nine.append(ninth_year)

ten = ["1973"]
ten.append(tenth_year)

eleven = ["1974"]
eleven.append(elev_year)


json = []
json.append(one)
json.append(two)
json.append(three)
json.append(four)
json.append(five)
json.append(six)
json.append(seven)
json.append(eight)
json.append(nine)
json.append(ten)
json.append(eleven)