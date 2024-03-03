import sys
# print ('argument list', sys.argv)
File = sys.argv[1]
# print ("selected: {}".format(File))

capitalizedWords = ["GOD", "YOU", "YOUR", "HOLY SPIRIT", "ТИ", "БОГ", "ТВІЙ", "ТВОЇ", "ДУХ СВЯТИЙ"]

def CapitalizeLetter(source: str):
	# print("should be letters: ",source)
	return source[0].capitalize() + source[1:].lower()

def SentenceCase(source: str):
	# print("should be words: ",source)
	# send the first word to be capitalized:
	firstWord = CapitalizeLetter(source[0])
	# send the rest of the sentence to be lowercase:
	restOfLine = firstWord
	for word in source[1:]:
		# if cond to check if word needs to be capitalized:
		if word in capitalizedWords:
			restOfLine += " " + CapitalizeLetter(word)
		else:
			restOfLine +=  " " + word.lower()
	# print("restOfLine: ",restOfLine)
	return restOfLine

with open(File, 'r') as data_file:
	with open('MkLoweroutput.txt', 'a') as output_file:
		for line in data_file:
			word_list = line.split()
			stringLength = len(line)
			# print("line length: ", stringLength)
			if stringLength <= 1:
				# line is empty
				print("")
			else:
				word_list = [SentenceCase(word_list)]
			output_file.write(" ".join(word_list) + "\n")
