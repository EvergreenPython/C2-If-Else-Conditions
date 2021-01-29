a = 200 
b = 33 

if (b > a): 
  print("b is greater than a")
else: 
  print("b is not greater than a")

# Write a conditional statement that evaluates if the user input is positive or negative 

a = 5000 # Hard coding 
num = int(input("Enter a number: "))
if(num > 0): 
  print("I see that your number is positive")
elif(num == 0): 
  print("You entered 0")
else: 
  print("It's negative")

# Ask the user for their age 
# If they are younger than 13, tell them they can only watch PG/G Movies
# If the are 13 and older but younger than 17, they can only watch PG-13/PG/G movies  
# If they are 17 and older, they can watch all movies

age = int(input("What is your age? "))
if(age < 13): 
  print("You can only PG/G movies")
elif(17 > age >= 13): 
  print("That means you can watch PG-13 and PG/G movies")
else: 
  print("You can watch all movies")

is_Hungry = False 
is_Sleepy = False 
if(is_Hungry == True): 
  print("You should go eat")
if(is_Sleepy == True): 
  print("You should go sleep")
if(is_Sleepy == False): 
  print("Wow you're well-rested")

# Ask the user for a number 
# Tell the user if their number is even or odd

userNum = int(input("Choose a number: "))

if(userNum % 2 != 0):
  print("Your number is odd")
else:
  print("Your number is even")