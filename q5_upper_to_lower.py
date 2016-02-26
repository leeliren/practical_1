# q5_upper_to_lower.py
# convert upper case letters to lower case

# input upper case letters
uppercase = input("enter uppercase character: ")

# convert to ASCII values
lowercase = ord(uppercase) + 32

# output lowercase letter
print(chr(lowercase))
