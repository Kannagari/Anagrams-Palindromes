def Ana(s1, s2):
	d = {}
	if len(s1) != len(s2):
		return False
	for c in s1:
		if c in d:
			d[c] = d[c] + 1
		else:
			d[c] = 1

	for c in s2:
		if c in d:
			d[c] = d[c] - 1
		else:
			return False

	for key in d:
		if d[key] != 0:
			return False
	return True

def Pal(s1):
	low = 0
	high = len(s1) - 1
	while low <= high:
		if s1[low] != s1[high]:
			return False
		low = low + 1
		high = high - 1
	return True

def main():
	print("Please enter two strings to see if they are anagrams.")
	s1 = str(input("Please enter string 1: " ))
	s2 = str(input("Please enter string 2: "  ))
	if Ana(s1,s2):
		print("These two strings are anagrams!\n")
	else:
		print("These two strings are not anagrams!\n")

	print("Please enter a string to check if it is a palindrome.")
	s3 = str(input("Please enter a string:"))
	if Pal(s3):
		print("This string is a palindrome!")
	else:
		print("This string is not a plaindrome!") 


if __name__ == '__main__':
	main()
