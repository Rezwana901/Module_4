print("Rezwana Sultana\n")
#a) You have deposited 20,000 BDT in bank for a compound interest of 5% per year. Which means, after one year
#your balance will be your principal + profit. For the next year (principal + profit) will be counted as
#your new principal and profit will be calculated on your new principal. And this will go on. What will be
#your money after 4 years. [Don’t use the formula C=P(1+r/100)n] [Use  in-Place operator]

x = 20000
x+= 20000*5/100 #1st year
x+= 21000*5/100 #2nd year
x+= 22050*5/100 #3rd year
x+= 23152*5/100 #4th year
print(x)
print("\n")

#b) Take all the following inputs of a user: Name, Birth year, Nationality, University/College Name, Living
#Country, Male/Female, and Mobile number (11 digit). DO NOT USE ANY IF ELSE or Advance CODE
#Then, give a output of his/her profile like following output 👇
#Name: Inputted Name here
#Age: *** years
#Nationality: ***
#University/College: ****
#Current Location: Inputted living country name
#Mobile Number: +8801**********
#Gender: True (if male), False (if female)

Name = input("Rezwana Sultana")
Birth_Year = input(1997)
Nationality = input("BANGLADESHI")
University_Name = input("University of Dhaka")
Living_Country = input("Bangladesh")
Gender = "Male" < "Female"
Mobile_Number = input("+8801521111111")

print(Name)
print(Birth_Year)
print(Nationality.upper())
print(University_Name)
print(Living_Country)
print(Mobile_Number[3:])
print(Gender)