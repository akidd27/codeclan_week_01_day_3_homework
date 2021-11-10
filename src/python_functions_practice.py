# write functions here
months = {
    1 : "January",
    2 : "February",
    3 : "March",
    4 : "April",
    5 : "May",
    6 : "June",
    7 : "July",
    8 : "August",
    9 : "September",
    10 : "October",
    11 : "November",
    12 : "December"
}

# print(months)
def return_10():
    return 10

def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(a,b):
    return int(a) + int(b)

def number_to_full_month_name(x):
    return months[x]

def number_to_short_month_name(number):
    return months[number][0:3]

def side_to_volume(side):
    return side **3

def reverse_string(string):
    return string[::-1]

def to_celcius(fahrenheit_temp):
    return (fahrenheit_temp-30)/2
