def isPalindrome(test):                                   # creating a function isPalindrome with test as its argument
    return test == test[::-1]                             # this function terminates after comparing test value and its reverse value
    

test = str(input())                                       # taking string input from user
answer = isPalindrome(test)                               # assigning our function result to variable answer

if answer:                                                # if else loop to check if answer is true it will print yes on being false it will print no
	print("Yes")
else:
	print("No")
