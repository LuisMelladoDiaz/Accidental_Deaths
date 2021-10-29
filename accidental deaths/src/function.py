import csv

from collections import namedtuple

gunviolence = namedtuple ('Gunviolence','date,state,county,address,killed,injured,operations')



def read_data (file):
    with open (file,encoding = 'utf-8') as f:
        reader = csv.reader (f)
        next(reader)
        data = [gunviolence(date,state,county,address,int(killed),int(injured),operations) for date,state,county,address,killed,injured,operations in reader]
        return data




