#Ask the user to enter a word or sentence and store it in 'string'
string = input("Enter a word or sentence: ")

#Create an empty string called 'string2'
string2 = ""

#Loop through each character 'i in 'string'
for i in string:
    # Add the character 'i' in front of 'string2'
    string2 = i + string2

#Print the original string ('string')
print("Original string:", string)

#Print the reversed string ('string2')
print("Reversed string:", string2)