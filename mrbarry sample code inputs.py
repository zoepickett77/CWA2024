
pay_amt = float(input("Enter your salary "))
Age = int(input("Enter your age "))
fName = str(input("enter your name "))
sName = input("enter your surname ")

gender_input = input("Please enter your gender (Male/Female): ")

gender_input = gender_input.lower()

if gender_input == "male":
    is_male = True
    is_female = False
elif gender_input == "female":
    is_male = False
    is_female = True
else:
    is_male = False
    is_female = False

print("")
print("")
print("")
print("Salary ", type(pay_amt), pay_amt,"\nFirst Name " ,type(fName), fName, "\nSurname ", type (sName),sName,)
print("\nAge ", type(Age),Age, "\nGender ", type(gender_input), gender_input)

print("\nIs Male:", is_male)
print("Is Female:", is_female)