
import math
import random

#=============================================================================
# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("value of pi :", pi, type(pi))

#=============================================================================
# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)

if i > 50 :
	print("value of i is grater than 50:", i) 
elif i < 50 :
	print("value of i is less than 50:", i) 
else : 
	print("value of i is equal to :", i) 

#=============================================================================
# TODO: Write a conditional that prints the color of the selected sportsball
picked_sportsball = random.choice(['tennis', 'basketball', 'golf','soccer'])

if picked_sportsball == 'tennis':
	print("pussy election, tennis ball is green")

elif picked_sportsball == 'basketball':
	print("good election, basketball is brown, usually...")

elif picked_sportsball == 'golf':
	print("worst election, golf is white, you dickface...")

else:
	print("Best election, soccer is white, bro, lets play.")

#=============================================================================
# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def by2(n_1,n_2):
	res= n_1*n_2
	return print ("the result is: " , res)

#=============================================================================
# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

print("12 x 96 ")
by2(12,96)

print("48 x 17 ")
by2(48,17)

print("196523 x 87323 ")
by2(196523,87323)

