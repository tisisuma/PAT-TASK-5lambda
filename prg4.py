#To Verify whether the email address is correct or not


# umamaheswari.be@yahoo.com
# 1.) alphanumeric characters
# 2.) there should be a @ symbol
# 3.) after @ symbol there is alphanumeric characters
# 4.) there should be a . symbols also
# 5.) after . symbol there should be 2 to 6 alphanumeric characters
import re
def validate_email(data):
    # search_pattern = '[a-zA-z0-9a-zA-]+@[Z0-9]'
    search_pattern = '[A-Za-z0-9._]+@[A-Za-z0-9]+.[A-Za-z]{2,6}'
    if re.fullmatch(search_pattern, data):
        return True
    else:
        return False


data = 'uma_maheswari.be@yahoo.com'
print(validate_email(data))

#To Verify whether the Bangladesh phone number is correct or not


# 880 1234567890
# 1.) starts with + sign and 880
# 2.) it should have 10 numbers



def validate_mobile_number(data):
    search_pattern = '^\+[880]+[0-9]\\d{10}$'
    if re.fullmatch(search_pattern, data):
        return True
    else:
        return False   
data = '+8801153067158'
print(validate_mobile_number(data))


#To Verify whether the USA  phone number is correct or not


# 4506788378
# 1.) Area code starts with + and (2-6)
# 2.) it should have 10 numbers

def mobile_number(data):
    search_pattern = '^\+[2-6]+[0-9]\\d{8}$'
    if re.fullmatch(search_pattern,data):
        return True
    else:
        return False
data = '+5146789008'
print(mobile_number(data))


#To verify password

#1.It should have 16 characters
#2.It should have both upper characters and lower characters 
#3.It should accept special Characters
#4.It should accept numbers


def password(data):
    search_pattern = '^[a-zA-Z0-9!@#$%^&*()_+=-~`<>.,/?:;"\|]{16}'
    if re.fullmatch(search_pattern,data):
        return True
    else:
        return False
data = 'Password@123$%!?'
print(password(data))
