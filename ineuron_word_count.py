# -*- coding: utf-8 -*-
"""ineuron_word_count.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11q0OHxA7kKwUMtAWddF76DN8h7KVRRCw
"""

pharse = "the quick brown fox jumped over lazy dogs quick dogs jumped jumped"

"""**mapper**"""

words = pharse.split()
number = [1 for i in range(len(words))]
for w,n in zip(words,number):
  print(w,n)

"""**shuffle sort**"""

def freq(pharse):

	# break the string into list of words
	pharse = pharse.split()		
	str2 = []

	# loop till string values present in list str
	for i in pharse:			

		# checking for the duplicacy
		if i not in str2:

			# insert value in str2
			str2.append(i)
			
	for i in range(0, len(str2)):

		# count the frequency of each word(present
		# in str2) in str and print
		print(str2[i], [ 1 for j in range(pharse.count(str2[i]))])


pharse = "the quick brown fox jumped over lazy dogs quick dogs jumped jumped"
freq(pharse)

"""**reduce -sum()**"""

##https://www.geeksforgeeks.org/calculate-the-frequency-of-each-word-in-the-given-string/
def printFrequency(strr):
	M = {}
	
	# string for storing the words
	word = ""
	
	for i in range(len(strr)):
		
		# Check if current character
		# is blank space then it
		# means we have got one word
		if (strr[i] == ' '):
			
			# If the current word	
			# is not found then insert
			# current word with frequency 1
			if (word not in M):
				M[word] = 1
				word = ""
			
			# update the frequency
			else:
				M[word] += 1
				word = ""
		
		else:
			word += strr[i]
	
	# Storing the last word of the string
	if (word not in M):
		M[word] = 1
	
	# Update the frequency
	else:
		M[word] += 1
		
	# Traverse the map
	# to print the frequency
	for it in M:
		print(it, M[it])
	
# Driver Code
pharse = "the quick brown fox jumped over lazy dogs quick dogs jumped jumped"
printFrequency(pharse)

# This code is contributed by shubhamsingh10

