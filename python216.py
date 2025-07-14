#Python Program to Count the Number of Vowels Present in a String using Sets


def vowel_count(str):
	count = 0
	vowel = set("aeiouAEIOU")
	for alphabet in str:
		if alphabet in vowel:
			count = count + 1
	print("No. of vowels :", count)
str = input("enter strings:")
vowel_count(str)