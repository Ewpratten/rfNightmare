def spawnMenu(title, options):
	print(f"{title}\n")
	valid_responses = []
	for i,option in enumerate(options):
		print(f"{i}) {option['text']}")
		valid_responses.append(i)
	
	print("\nPlease pick")
	try:
		response = int(input(">"))
	except:
		#useless data
		response = 10000000000000
	
	if response in valid_responses:
		options[response - 1]["callback"]()
	else:
		print("Invalid answer")
		spawnMenu(title, options)