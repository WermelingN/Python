from datetime import date

users = list()
birthdays = list()
numberofusers = int(input("How many users are there?: "))

i = 0

while i < numberofusers:
	users.append(input("What is user " + str(i + 1) + "'s name?: "))
	birthdays.append(input("What is user " + str(i + 1) + "'s birthday? (use dd/mm/yyyy): "))

	while birthdays[i][2] != "/" or birthdays[i][5] != "/":
		print("Invalid Format, try again")
		birthdays[i] = input("What is user " + str(i + 1) + "'s birthday? (use dd/mm/yyyy): ")

	i = i + 1





#name is inherited, User1 should become the input name
#User1 = Username1[0].upper() + Username1[1:]
#User2 = Username2[0].upper() + Username2[1:]
#User3 = Username3[0].upper() + Username3[1:]

#Ask user for their date of birth
#ensure user has input correct birthdate format
#User1DOB = input(User1 + ", what is your birth date? (use dd/mm/yyyy): ")
#while User1DOB[2] != "/" or User1DOB[5] != "/":
#	print("Invalid Format, Try Again")
#	User1DOB = input(User1 + ", what is your birth date? (use dd/mm/yyyy): ")


#User2DOB = input(User2 + ", what is your birth date? (use dd/mm/yyyy): ")
#while User2DOB[2] != "/" or User2DOB[5] != "/":
#	print("Invalid Format, Try Again")
#	User2DOB = input(User2 + ", what is your birth date? (use dd/mm/yyyy): ")

#User3DOB = input(User3 + ", what is your birth date? (use dd/mm/yyyy): ")
#while User3DOB[2] != "/" or User3DOB[5] != "/":
#	print("Invalid Format, Try Again")
#	User3DOB = input(User3 + ", what is your birth date? (use dd/mm/yyyy): ")



#User1Age = int(input(User1 + ", what is your age?: "))
#User2Age = int(input(User2 + ", what is your age?: "))
#User3Age = int(input(User3 + ", what is your age?: "))

#print(User1, "You will turn 100-years-old in ", 100 - User1Age, "years.")
#print(User2, "You will turn 100-years-old in ", 100 - User1Age, "years.")
#print(User3, "You will turn 100-years-old in ", 100 - User1Age, "years.")


#.split("/")