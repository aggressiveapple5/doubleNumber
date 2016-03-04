error = True
while error == True:
	number = raw_input("What number should I double? ")

	try: 
		number = float(number)
		#Try is only for things that might not work
	except ValueError:
		print("Sorry that's not a number. ")
		print("Try again.")
		error = True
	
	
	else:
		print("Double that is {}.".format(number * 2))
		error = False
		
	
	
	
	
