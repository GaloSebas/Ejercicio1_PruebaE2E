import json
import os
import random

from faker import Faker
from datetime import datetime
from dateutil.relativedelta import relativedelta

def generate_fake_data():
    fake = Faker()
    first_name = fake.first_name()
    last_name = fake.last_name()
    name = first_name + ' ' + last_name
    country = fake.country()
    city = fake.city()
    credit_card = random.randint(1111111111111111,9999999999999999)
    month = fake.month()
    year = fake.year()
    return name, country, city, credit_card, month, year

def get_today_date():
        #Get todays date
        today = datetime.now()
        adjusted_date = today - relativedelta(months=1)
        day = adjusted_date.day
        month = adjusted_date.month
        year = adjusted_date.year
        #Sets the formatting for the date
        formatted_date = f"{day}/{month}/{year}"
        return formatted_date

#Path where the json file will be stored
VARIABLES_FILE = './utils/global.json'

def ensure_file_exists():
    #Validate if the file exists if not it generates it
    if not os.path.exists(VARIABLES_FILE):
        with open(VARIABLES_FILE, 'w') as file:
            json.dump({}, file)

def set_variable(key, value):
    #Validate if the json file exists
    ensure_file_exists()
    #Reads the current variables
    with open(VARIABLES_FILE, 'r') as file:
        variables = json.load(file)
    #Adds the new variable
    variables[key] = value
    #Writes the new variable into the json file
    with open(VARIABLES_FILE, 'w') as file:
        json.dump(variables, file, indent=4)

def get_variable(key):
    #Validate if the json file exists
    ensure_file_exists()
    #Reads the current variables
    with open(VARIABLES_FILE, 'r') as file:
        variables = json.load(file)
    #Returns the value from the inputed key (If the key doesn´t exists then it answres an error)
    if key in variables:
        return variables[key]
    else:
        raise KeyError(f"La variable '{key}' no existe.")
