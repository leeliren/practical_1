# q4_sum_digits.py
# conpute sum of digits in integer

# input integer
num = int(input("enter integer (0-1000): "))

#conpute sum of digits
total = 0
total = total + (num%10) # add last remainder digit
num = num//10            # remove last digit
total = total + (num%10)
num = num//10
total = total + (num%10)
num = num//10

# output sum
print ("sum of digits", total)
