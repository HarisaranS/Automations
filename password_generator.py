import string 
import random 
from csv  import writer 

def passgen():

    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    platform = input("Enter the platform for which you want to generate the password:") 
    passlen = int(input("Enter the length of the password:"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    password = ("".join(s[0:passlen]))
    print(password)
    pass_data = [platform, password]
    with open("path/to/csv_file",'a') as f:
        write_data = writer(f)
        write_data.writerow(pass_data)

passgen()