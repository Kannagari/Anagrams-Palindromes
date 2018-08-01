def Ana(s1, s2): #Function to check if the passed strings are anagrams
	d = {} #Create an empty dictionary for anagram checking
	if len(s1) != len(s2): #If the strings are not the same length, they cannot be anagrams
		return False
	for c in s1: #For every character in the first string
		if c in d: #If the current character is already in the dictionary
			d[c] = d[c] + 1 #Increase the number of occurences of that character
		else:
			d[c] = 1 #Else, initiate the value for that character to 1

	for c in s2: #For every character in s2
		if c in d: #If the character is already found in the dictionary
			d[c] = d[c] - 1 #Decrement the number of occurences
		else:
			return False #If the character is not in the dictionary already, it is not an anagram

	for key in d: #for every key in in the dictionary
		if d[key] != 0: #If the value is not zero, then we have leftover characters
			return False #As such, the two strings are not palindromes
	return True #If we've passed all checks, return true

def Pal(s1): #Function to check if the passed string is a palindrome
	low = 0 #Create a index check for the beginning of the string
	high = len(s1) - 1 #Create a index walker for the beginning of the string
	while low <= high: 
		if s1[low] != s1[high]: #If the characters at the end and beginning of the string are not equal
			return False #The string is not a palindrome, return false
		low = low + 1 #Walk the indexes forward and backward respectively to check the entire string
		high = high - 1
	return True #If we passed the check, return true

def main():
	print("Please enter two strings to see if they are anagrams.")
	s1 = str(input("Please enter string 1: " )) #Getting string input from user
	s2 = str(input("Please enter string 2: "  )) #Getting string input from user
	if Ana(s1,s2): #Calling Ana and reacting based off its return value
		print("These two strings are anagrams!\n")
	else:
		print("These two strings are not anagrams!\n")

	print("Please enter a string to check if it is a palindrome.")
	s3 = str(input("Please enter a string:")) #Getting string input from user
	if Pal(s3): #Calling Pal and reacting based off its return value
		print("This string is a palindrome!")
	else:
		print("This string is not a palindrome!") 


if __name__ == '__main__':
	main()
