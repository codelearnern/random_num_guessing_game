# Import random module
import random

# Generates random number between 1 and 100
print("Please enter a number between 1 and 100")
random_num = random.randint(1, 100)

# Lets user guess the number and then converts that to integer 
user_inp = int(input())

# While user_inp is not equal to random_num...
while user_inp != random_num:

	# While user_inp is greater than random_num...
	while user_inp > random_num:
		print("Your number is greater than the random number.  Please try again.")

		# Gives user another try
		user_inp = int(input())

	# While user_inp is less than random_num...
	while user_inp < random_num:
		print("Your number is less than the random number.  Please try again.")

		# Gives user another try
		user_inp = int(input())

# If it is equal to random_num...
print("Good job, you guessed the number!")