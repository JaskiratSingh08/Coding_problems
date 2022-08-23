def reverseString(testString):                # creating a new function called reverseString whivh takes testString as argument
  str = ""                                    # initialised a variable called str which is empty
  for i in testString:                        # a loop which will run upto length of our testString value
    str = i + str                             # iterating each character and joing it to make our final reverse string
  return str                                  # to return the str value when the fuction is called and finished executing

  # or instead of writting above four lines, just:
  # str = testString[::-1]                                                # created a variable str, we iterate through our testString from last character and
                                                                          # asign the value to str after iterating
  

testString = input()                          # testString is getting assigned the value which is taken from user as input
print(reverseString(testString))              #calling the function reverseString by pssing the input value and printing the output.
