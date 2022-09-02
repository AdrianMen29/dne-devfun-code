#Adding 2 numbers

print("For quit, please type EXIT at any time")

while True:
	try:

		print("Type Number 1 :")
		n_1= float(input())

		print("Type Number 2 :")
		n_2= float(input())

		sum=n_1+n_2
		print("Total is :", sum)

	except (ValueError,NameError):
		if n_1 or n_2 == "EXIT":
			break
		else:

			print("please type correctly u fucking retard, enter only NUMERICAL values")
